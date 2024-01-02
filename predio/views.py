from django.shortcuts import render, redirect
from .models import Predio, Propietario
from dominios.models import TipoNumeroDocumento
from .forms import CreatePredioForm,CreatePropietarioForm
from .forms import PredioEditForm,PropietarioEditForm
from django.http import JsonResponse

#listar predios
def index(request):
    propietarios_creados = Propietario.objects.all()
    predios_creados = Predio.objects.all()
    print(predios_creados)
    return render(request,'index.html',{'predios':predios_creados,'propietarios':propietarios_creados})

#crear un predio
def create_predio(request):
    if request.method == 'POST':
        form = CreatePredioForm(request.POST)
        if form.is_valid():
            predioGuardado = form.save(commit=False)
            predioGuardado.save()  
            predioGuardado.propietarios.set(form.cleaned_data['propietarios'])

            return JsonResponse({'success': True})

        # Si el formulario no es válido, devuelve los errores en formato JSON
        errors = {'form_errors': form.errors}
        return JsonResponse(errors, status=400)

    else:
        form = CreatePredioForm()

    return render(request, 'index.html', {'form': form})


#Eliminar Predio
def delete_predio(request,id):
    delete_predio=Predio.objects.get(id=id)
    delete_predio.delete()
    return redirect('/?mensaje=Predio Eliminado Exitosamente')

#Editar Predio
def edit_predio(request,id):
    propietarios_creados = Propietario.objects.all()
    predioObtenido= Predio.objects.get(id=id)
    forms = PredioEditForm(request.POST or None, instance=predioObtenido)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/?mensaje=Predio Actualizado Exitosamente')
    return render(request,'edit_predio.html',{'forms':forms,'propietarios':propietarios_creados})

#Mostrar Formulario Para Registrar Propietario
def mostrar_formulario(request):
    return render(request, 'registrar_propietarios.html')

#Crear Propietario
def create_propietario(request):
    if request.method == 'POST':
        form = CreatePropietarioForm(request.POST)
        if form.is_valid():
            propietarioGuardado = Propietario(
                nombrePropietario=form.cleaned_data['nombrePropietario'],
                tipoPropietario=form.cleaned_data['tipoPropietario'],
                numeroDocumento=form.cleaned_data['numeroDocumento'],
                tipoDocumento=form.cleaned_data['tipoDocumento'],
            )
            propietarioGuardado.save()
            return JsonResponse({'success': True})

        # Si el formulario no es válido, devuelve los errores en formato JSON
        errors = {'form_errors': form.errors}
        return JsonResponse(errors, status=400)

    else:
        form = CreatePropietarioForm()
    return render(request, 'registrar_propietarios.html', {'form': form})

def ver_propietarios(request):
    tipo_documento = TipoNumeroDocumento.objects.all()
    propietarios_creados = Propietario.objects.all()
    return render(request,'ver_propietarios.html',{'propietarios':propietarios_creados,'tipoDocumento':tipo_documento})

def delete_propietario(request,id):
    eliminar_propietario=Propietario.objects.get(id=id)
    eliminar_propietario.delete()
    return redirect('/ver_propietarios?mensaje=Usuario Eliminado Exitosamente')

#Editar Propietario
def edit_propietario(request,id):
    propietarioObtenido= Propietario.objects.get(id=id)
    forms = PropietarioEditForm(request.POST or None, instance=propietarioObtenido)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/ver_propietarios?mensaje=Propietario Actualizado Exitosamente')
    return render(request,'edit_propietario.html',{'forms':forms})




