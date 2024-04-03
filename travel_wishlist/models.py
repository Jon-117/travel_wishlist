from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no-photo'
        visited_message = f"was visited on {self.date_visited}"
        not_visited_message = "has not been visited yet"
        return f'{self.pk}: {self.name} {visited_message if self.visited else not_visited_message}\nPhoto: {photo_str}'
        # return f'{"✔ I went to " if self.visited else "✘ I have not yet visited "}{self.name}'
