from django.db import models
from django.utils import timezone

# book model with name, pagenumber, genre, publish date attributes
class Book(models.Model):
    name = models.CharField(max_length=200)
    pageNumber = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    # pub_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.name


# car model with make, model, year attributes

class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    # year = models.DateField()



    def __str__(self):
        return self.make