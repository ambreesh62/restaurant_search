from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


