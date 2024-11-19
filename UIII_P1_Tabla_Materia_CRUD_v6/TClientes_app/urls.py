from django.urls import path
from TClientes_app import views

urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<clienteid>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente"),
    path("borrarCliente/<clienteid>",views.borrarCliente,name="borrarCliente")
]
