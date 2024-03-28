from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length =200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{"✔ I went to " if self.visited else "✘ I have not yet visited "}{self.name}'
