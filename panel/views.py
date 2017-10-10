from django.shortcuts import render
from .models import Contratista
from .models import *
from .models import Maquinaria
from django.http import HttpResponse
import json

def home(request):
    return render(request,'panel/base.html',{})

def admin(request):
    return render(request, 'panel/register_ot.html', {})

def load_contratistas(request):
    contratistas = Contratista.objects.all()
    contratistas = [ contra_serialize(contratista) for contratista in contratistas ]
    return HttpResponse(json.dumps(contratistas), content_type='application/json')

def contra_serialize(contratista):
    return {'id': contratista.id , 'nombres': (contratista.nombres + ' ' + contratista.apellidos)};

def load_maquinaria(request):
    contratista_id = request.GET.get("id_contratista")
    contratista = Contratista.objects.get(pk=contratista_id)
    maq_conts = ContratistaMaquinaria.objects.filter(contratista=contratista).select_related()
    maquinarias = [maqu_serialize(maq_cont) for maq_cont in maq_conts]
    return HttpResponse(json.dumps(maquinarias), content_type='application/json')


def maqu_serialize(maq_cont):
    return {'id': maq_cont.maquinaria.id,"descripcion": maq_cont.maquinaria.descripcion}

def load_mantenimiento(request):
    tipo_mantenimientos = TipoMantenimiento.objects.all()
    tipo_mantenimientos = [mantenimiento_serialize(tipo_mantenimiento) for tipo_mantenimiento in tipo_mantenimientos]
    return HttpResponse(json.dumps(tipo_mantenimientos), content_type='application/json')

def mantenimiento_serialize(tipo_mantenimiento):
    return {'id': tipo_mantenimiento.id , 'descripcion': tipo_mantenimiento.descripcion};

def load_parroquia(request):
    parroquias = Parroquia.objects.all()
    parroquias = [parroquia_serialize(parroquia) for parroquia in parroquias]
    return HttpResponse(json.dumps(parroquias), content_type='application/json')

def parroquia_serialize(parroquia):
    return {'id': parroquia.id, 'descripcion': parroquia.descripcion};

def load_actividad(request):
    actividades = TipoActividad.objects.all().select_related()
    actividades = [actividad_serialize(actividad) for actividad in actividades]
    return HttpResponse(json.dumps(actividades),content_type='application/json')

def actividad_serialize(actividad):
    return {'id': actividad.id, 'descripcion': actividad.descripcion};