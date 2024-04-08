from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, TripReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages


@login_required
# Create your views here.
def place_list(request):  # must have 1 arg: request

    if request.method == 'POST':  # Create new Place
        form = NewPlaceForm(request.POST)
        place = form.save(commit=False)  # Creates a model object from form inputs
        place.user = request.user
        if form.is_valid():  # Validation against DB constraints
            place.save()     # Saves place to DB
            return redirect('place_list')  # Reloads home page (which we've named 'place_list')



    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    # places = Place.objects.all()
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def about(request):
    author = 'Jon'
    about = "A basic travel wishlist app"
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})


@login_required
def visited(request):
    visited = Place.objects.filter(user=request.user).filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden()
    return redirect('place_list')


@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user != request.user:
        return HttpResponseForbidden()
        # render(request, ')travel_wishlist/place_detail.html', {'place': place})

    # Does it belong to current user?

    # is this a GET request (show data and form), or a POST request (update place object)
    # if POST, validate form data & update.
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            messages.info(request, 'Trip information has been updated.')
        else:
            messages.error(request, form.errors) # TODO - Refine later
        return redirect('place_details', place_pk=place.pk)

    else:
        # if GET, show place & form
        # if place is visited show form, else no form shown.
        if place.visited:
            reveiw_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/place_detail.html', {'place':place, 'reveiw_form': reveiw_form})
        else:
            return render(request, 'travel_wishlist/place_detail.html', {'place':place})



@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()