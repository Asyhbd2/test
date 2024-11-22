from django.shortcuts import render
from .models import TCliente
# Create your views here.

def inicio_vista(request):
    losclientes=TCliente.objects.all()
    return render(request,"Index.html",{"misclientes":losclientes})
