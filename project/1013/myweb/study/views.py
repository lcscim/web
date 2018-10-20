from django.shortcuts import render

# Create your views here.
def index(req):
    num=10
    return render(req,"index.html",locals())
def shopping_car(req):
    num=10
    return render(req,"shopping_car.html",locals())
