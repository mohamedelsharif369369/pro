from django.shortcuts import render,redirect,get_object_or_404
from .models import Manzom



# Create your views here.

def manzom(request):
    manzom = Manzom.objects.all()
    return render(request,'manzom/manzom.html',{'manzom':manzom})




