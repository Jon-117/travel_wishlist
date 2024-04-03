from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name = 'place_list'),
    path('about', views.about, name = 'about'),
    path('visited', views.visited, name = 'visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name = 'place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name = 'place_details')
]
