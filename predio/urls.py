from django.urls import path
from .views import index, create_predio,delete_predio,edit_predio,mostrar_formulario,create_propietario,ver_propietarios,delete_propietario,edit_propietario

urlpatterns = [
    path('', index, name='index'),
    path('create_predio/', create_predio, name='create_predio'),
    path('delete_predio/<int:id>', delete_predio, name='delete_predio'),
    path('edit_predio/<int:id>', edit_predio, name='edit_predio'),
    path('mostrar_formulario', mostrar_formulario, name='mostrar_formulario'),
    path('create_propietario',create_propietario,name='create_propietario'),
    path('ver_propietarios',ver_propietarios,name='ver_propietarios'),
    path('delete_propietario/<int:id>',delete_propietario,name="delete_propietario"),
    path('edit_propietario/<int:id>',edit_propietario,name="edit_propietario")
]