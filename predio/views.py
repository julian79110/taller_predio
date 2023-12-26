from django.shortcuts import render, redirect
from .models import predio, propietario
from .editP import createPredio,createPropietario
from .editP import predioEdit,propietarioEdit
from django.http import JsonResponse

#listar predios
def index(request):
    predios_creados = predio.objects.all()
    print(predios_creados)
    return render(request,'index.html',{'predios':predios_creados})

#crear un predio
def create_predio(request):
    if request.method == 'POST':
        form = createPredio(request.POST)
        if form.is_valid():
            predioGuardado = predio(
                nombre=form.cleaned_data['nombre'],
                numeroCatastral=form.cleaned_data['numeroCatastral'],
                numeroMatricula=form.cleaned_data['numeroMatricula'],
                tipo=form.cleaned_data['tipo'],
                propietario=form.cleaned_data['propietario']
            )
            predioGuardado.save()
            return JsonResponse({'success': True})

        # Si el formulario no es válido, devuelve los errores en formato JSON
        errors = {'form_errors': form.errors}
        return JsonResponse(errors, status=400)

    else:
        form = createPredio()

    return render(request, 'index.html', {'form': form})

#Eliminar Predio
def delete_predio(request,id):
    delete_predio=predio.objects.get(id=id)
    delete_predio.delete()
    return redirect('/?mensaje=Predio Eliminado Exitosamente')

#Editar Predio
def edit_predio(request,id):
    predioObtenido= predio.objects.get(id=id)
    forms = predioEdit(request.POST or None, instance=predioObtenido)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/?mensaje=Predio Actualizado Exitosamente')
    return render(request,'edit_predio.html',{'forms':forms})

#Mostrar Formulario Para Registrar Propietario
def mostrar_formulario(request):
    return render(request, 'registrar_propietarios.html')

#Crear Propietario
def create_propietario(request):
    if request.method == 'POST':
        form = createPropietario(request.POST)
        if form.is_valid():
            propietarioGuardado = propietario(
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
        form = createPropietario()
    return render(request, 'registrar_propietarios.html', {'form': form})

def ver_propietarios(request):
    propietarios_creados = propietario.objects.all()
    return render(request,'ver_propietarios.html',{'propietarios':propietarios_creados})

def delete_propietario(request,id):
    eliminar_propietario=propietario.objects.get(id=id)
    eliminar_propietario.delete()
    return redirect('/ver_propietarios?mensaje=Usuario Eliminado Exitosamente')

#Editar Propietario
def edit_propietario(request,id):
    propietarioObtenido= propietario.objects.get(id=id)
    forms = propietarioEdit(request.POST or None, instance=propietarioObtenido)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/ver_propietarios?mensaje=Propietario Actualizado Exitosamente')
    return render(request,'edit_propietario.html',{'forms':forms})