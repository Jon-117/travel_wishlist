from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm


# Create your views here.
def place_list(request):  # must have 1 arg: request

    if request.method == 'POST':  # Create new Place
        form = NewPlaceForm(request.POST)
        place = form.save()  # Creates a model object from form inputs
        if form.is_valid():  # Validation against DB constraints
            place.save()     # Saves place to DB
            return redirect('place_list')  # Reloads home page (which we've named 'place_list')

    places = Place.objects.filter(visited=False).order_by('name')
    # places = Place.objects.all()
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def about(request):
    author = 'Jon'
    about = "A basic travel wishlist app"
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})


def visited(request):
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    return redirect('place_list')

