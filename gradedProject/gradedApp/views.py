
from django.http import HttpResponse
from .models import Book
from .models import Car


def index(request):
    return HttpResponse("<h1>Carlos's Graded Class Work<h1>")

def newBook(request):
    print("newbook")
    newObject = Book(name="IT", pageNumber= 356,  genre="Horror",
                     )
    newObject.save()
    return HttpResponse(newObject)

# car model
def newCar(request):
    newCar = Car(make="Mustang", model = "Ford", )
    newCar.save()
    print(newCar)
    return HttpResponse(newCar)

# book model
def all(request):
    allBooks = ""
    allObjects = Book.objects.all()

    for eachElement in allObjects:
        allBooks+= eachElement.objects.filter(year__gt = 2001)
        return HttpResponse(allBooks)

def allCarModels(request):
    allCars = ""
    allCarObjects = Book.objects.all()

    for eachElement in allCarObjects:
        allCars+= eachElement.objects.filter(year__gt = 2010)
        return HttpResponse(allCars)