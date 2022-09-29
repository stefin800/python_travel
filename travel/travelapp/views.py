from django.shortcuts import render
from . models import travelmodel
from . models import travelpost

# Create your views here.
def home(request):
    obj=travelmodel.objects.all()
    obj1=travelpost.objects.all()
    return render(request,"index.html",{'result':obj,'postresult':obj1})