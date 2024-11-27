from django.urls import path
from TProductos_app import views

urlpatterns = [
    path("producto",views.inicio_vistaProducto,name="inicio_vistaProducto"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<productoid>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<productoid>",views.borrarProducto,name="borrarProducto")
]
