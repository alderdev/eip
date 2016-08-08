from django.shortcuts import render

from .models import Department, Jobtitle, Person

# Create your views here.
def showPerson(request):
    title = "Person Detail"

    return render(request, "persondetail.html", locals())
