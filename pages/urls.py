from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/cities/', views.cities_dashboard, name='cities_dashboard'),
    path('dashboard/attractions/', views.attractions_dashboard, name='attractions_dashboard'),
    path('dashboard/reviews/', views.reviews_dashboard, name='reviews_dashboard'),
    path('dashboard/wishlist/', views.wishlist_dashboard, name='wishlist_dashboard'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('cookie/', views.cookie, name='cookie'),
]
