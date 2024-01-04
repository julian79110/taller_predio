from django.shortcuts import render, redirect
from .models import Predio, Propietario
from dominios.models import TipoNumeroDocumento
from .forms import CreatePredioForm,CreatePropietarioForm
from .forms import PredioEditForm,PropietarioEditForm
from django.http import JsonResponse

#permisos
#herencia
#include django template

#listar predios
def index(request):
    """
        Listar Los predios Y los propietarios
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista
 
        :return: listado de predios y propietarios
        :rtype: HttpResponse
    """
    #trae todos los registros de la tabla propietarios
    propietarios_creados = Propietario.objects.all()
    #trae todos los registros de la tabla predios
    predios_creados = Predio.objects.all()
    #la respuesta de esta funcion renderiza index.html y le enviamos los diccionario de predio y propietario
    return render(request,'index.html',{'predios':predios_creados,'propietarios':propietarios_creados})

#crear un predio
def create_predio(request):
    """
        Crear Un Predio
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista
 
        :return: respuesta ajax con el mensaje de exito
        :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = CreatePredioForm(request.POST)
        if form.is_valid():
            #aun no guarda los cambios en la base de datos mientras busca errores
            predioGuardado = form.save(commit=False)
            #guarda los registros
            predioGuardado.save()
            #mantiene los datos escritos  
            predioGuardado.propietarios.set(form.cleaned_data['propietarios'])
            #retorna la respuesta en formato JSON
            return JsonResponse({'success': True})
            # Si el formulario no es válido, devuelve los errores en formato JSON
        errors = {'form_errors': form.errors}
        return JsonResponse(errors, status=400)
    else:
        form = CreatePredioForm()

    return render(request, 'index.html', {'form': form})


#Eliminar Predio
def delete_predio(request,id):
    """
        Eliminar predio
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista,
        :param id(Predio)
 
        :return: respuesta ajax con el mensaje de exito
        :rtype: HttpResponse
    """
    #obtiene el id de la db
    delete_predio=Predio.objects.get(id=id)
    #lo elimina de la db
    delete_predio.delete()
    return redirect('/?mensaje=Predio Eliminado Exitosamente')

#Editar Predio
def edit_predio(request,id):
    """
        Editar Predio
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista,
        :param id(Predio)
 
        :return: respuesta ajax con el mensaje de exito
        :rtype: HttpResponse
    """
    propietarios_creados = Propietario.objects.all()
    predioObtenido= Predio.objects.get(id=id)
    forms = PredioEditForm(request.POST or None, instance=predioObtenido)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/?mensaje=Predio Actualizado Exitosamente')
    return render(request,'edit_predio.html',{'forms':forms,'propietarios':propietarios_creados})

#Mostrar Formulario Para Registrar Propietario
def mostrar_formulario(request):
    """
        Renderizar el formulario para el registro de propietarios
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista

        :return: formulario para el registro de propietarios
        :rtype: HttpResponse
    """
    return render(request, 'registrar_propietarios.html')

#Crear Propietario
def create_propietario(request):
    """
        Recibe los datos del formulario y los guarda en la db
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista

        :return: Respuesta Mensaje de exito
        :rtype: HttpResponse
    """
    mensaje = None
    if request.method == 'POST':
        form = CreatePropietarioForm(request.POST)
        #si el formulario es valido pasa los datos
        if form.is_valid():
            propietarioGuardado = Propietario(
                nombrePropietario=form.cleaned_data['nombrePropietario'],
                tipoPropietario=form.cleaned_data['tipoPropietario'],
                numeroDocumento=form.cleaned_data['numeroDocumento'],
                tipoDocumento=form.cleaned_data['tipoDocumento'],
            )
            propietarioGuardado.save()
            mensaje='Propietario Creado Con Exito'
        else:
            pass
    else:
        form = CreatePropietarioForm()
    return render(request, 'registrar_propietarios.html', {'form': form, 'mensaje':mensaje})

def ver_propietarios(request):
    """
        Listar Los propietarios
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista
 
        :return: listado de propietarios
        :rtype: HttpResponse
    """
    tipo_documento = TipoNumeroDocumento.objects.all()
    propietarios_creados = Propietario.objects.all()
    return render(request,'ver_propietarios.html',{'propietarios':propietarios_creados,'tipoDocumento':tipo_documento})

def delete_propietario(request,id):
    """
        Eliminar propietario
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista,
        :param id(Propietario)
 
        :return: respuesta ajax con el mensaje de exito
        :rtype: HttpResponse
    """
    eliminar_propietario=Propietario.objects.get(id=id)
    eliminar_propietario.delete()
    return redirect('/ver_propietarios?mensaje=Usuario Eliminado Exitosamente')

#Editar Propietario
def edit_propietario(request,id):
    """
        Editar Propietario
 
        :author: Julian Tique - julian.tique@arcerojas.com
 
        :param request(HttpRequest): peticion de entrada de la vista,
        :param id(Propietario)
 
        :return: respuesta ajax con el mensaje de exito
        :rtype: HttpResponse
    """
    propietarioObtenido= Propietario.objects.get(id=id)
    forms = PropietarioEditForm(request.POST or None, instance=propietarioObtenido)
    #si el formulario es valido y la solicitud y es POST que me guarde 
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/ver_propietarios?mensaje=Propietario Actualizado Exitosamente')
    return render(request,'edit_propietario.html',{'forms':forms})




