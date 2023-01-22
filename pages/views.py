from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cities.models import City
from places.models import Attractions
from reviews.models import ReviewRating


# Create your views here.
@login_required
def dashboard(request):
    u_reviews = ReviewRating.user_reviews.user_reviews_query(user=request.user)
    sa_reviews = ReviewRating.user_reviews.reviews_staff_admin_check()
    cities = City.cities.staff_cities(user=request.user)
    attractions = Attractions.attraction.staff_attractions(user=request.user)
    user_wishlist = Attractions.attraction.wishlist_user(wishlist=request.user)
    context = {
        'u_reviews': u_reviews,
        'sa_reviews': sa_reviews,
        'cities': cities,
        'attractions': attractions,
        'user_wishlist': user_wishlist,
        'section': "dashboard",
    }
    return render(request, 'dashboard/dashboard.html', context)


@staff_member_required(login_url='/accounts/login/')
def cities_dashboard(request):
    cities = City.cities.staff_cities(user=request.user)
    context = {
        'cities': cities,
    }
    return render(request, 'dashboard/city/cities_list.html', context)


@staff_member_required(login_url='/accounts/login/')
def attractions_dashboard(request):
    attractions = Attractions.attraction.staff_attractions(user=request.user)
    context = {
        'attractions': attractions,
    }
    return render(request, 'dashboard/attractions/attractions_list.html', context)


@login_required
def reviews_dashboard(request):
    u_reviews = ReviewRating.user_reviews.user_reviews_query(user=request.user)
    sa_reviews = ReviewRating.user_reviews.reviews_staff_admin_check()
    context = {
        'u_reviews': u_reviews,
        'sa_reviews': sa_reviews,
    }
    return render(request, 'dashboard/reviews/reviews.html', context)


@login_required
def wishlist_dashboard(request):
    user_wishlist = Attractions.attraction.wishlist_user(wishlist=request.user)
    context = {
        'user_wishlist': user_wishlist,
    }
    return render(request, 'dashboard/wishlist/wishlist.html', context)


def home(request):
    cities = City.cities.cities_active()[:6]
    atractions = Attractions.attraction.attractions_active()[:4]
    context = {
        'cities': cities,
        'atractions': atractions,
        'section': 'home',
    }
    return render(request, 'pages/homepage.html', context)


def terms(response):
    return render(response, "pages/terms_and_conditions.html", )


def privacy(response):
    return render(response, "pages/policy_privacy.html", )


def cookie(response):
    return render(response, "pages/coockies.html", )
