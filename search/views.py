from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from cities.models import City
from places.models import Attractions
from search.forms import SearchForm


# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None


def results(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        city_list = City.cities.cities_active()
        atractions_list = Attractions.attraction.attractions_active()
        type_search = form.cleaned_data['type_search']
        s_word = form.cleaned_data['keyword_q']
        if type_search == 1:
            if is_valid_queryparam(s_word):
                city_list = city_list.filter(Q(name__icontains=s_word))
                paginator = Paginator(city_list, 1)  # Show 1 contacts per page.

                page_number = request.GET.get('page')
                cities = paginator.get_page(page_number)
                context = {
                    'cities': cities,
                    's_word': s_word,
                    'type_search': type_search,
                }
                return render(request, 'search/results.html', context)
        elif type_search == 2:
            if is_valid_queryparam(s_word):
                atractions_list = atractions_list.filter(Q(name__icontains=s_word))
                paginator = Paginator(atractions_list, 1)  # Show 1 contacts per page.
                page_number = request.GET.get('page')
                atractions = paginator.get_page(page_number)
                context = {
                    'atractions': atractions,
                    's_word': s_word,
                    'type_search': type_search,
                }
                return render(request, 'search/results.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Please fill in all fields correctly and try again.',
                                 extra_tags='danger')
            return redirect('pages:home')
    else:
        messages.add_message(request, messages.ERROR, 'Please fill in all fields correctly and try again.',
                             extra_tags='danger')
        return redirect('pages:home')
