from django.shortcuts import render,redirect
from .models import TProductos
# Create your views here.

def inicio_vistaProducto(request):
    losproductos=TProductos.objects.all()
    return render(request,"gestionarProducto.html",{"misproductos":losproductos})

def registrarProducto(request):
    
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["decimalprecio"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["intstock"]
    fechaingreso=request.POST["dateingreso"]

    guardarProducto=TProductos.objects.create(
        nombre=nombre,descripcion=descripcion,precio=precio,categoria=categoria,stock=stock,fechaingreso=fechaingreso
    )
    return redirect("inicio_vistaProducto")

def seleccionarProducto(request,productoid):
    producto=TProductos.objects.get(productoid=productoid)
    return render(request,"editarProducto.html",{"misproductos":producto})

def editarProducto(request,productoid):
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["decimalprecio"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["intstock"]
    fechaingreso=request.POST["dateingreso"]

    Producto=TProductos.objects.get(productoid=productoid)
    Producto.productoid=productoid
    Producto.nombre=nombre
    Producto.descripcion=descripcion
    Producto.precio=precio
    Producto.categoria=categoria
    Producto.stock=stock
    Producto.fechaingreso=fechaingreso
    Producto.save() # GUARDA REGISTRO ACTUAL
    return redirect("inicio_vistaProducto")

def borrarProducto(request,productoid):
    producto=TProductos.objects.get(productoid=productoid)
    producto.delete() # BORRA EL REGISTRO
    return redirect("inicio_vistaProducto")
