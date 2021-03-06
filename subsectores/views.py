from django.shortcuts import render, get_object_or_404
from .models import RegistroPlanAnual, CHOICES_MESES, DatosGenerales
from .forms import *
# Create your views here.


def consulta_proyectos(request, template='subsectores/consulta_proyectos.html'):
	proyectos = DatosGenerales.objects.all()
	return render(request, template, locals())

def list_informe(request, template='admin/lista_informe_plan_anual.html'):
	plan_anual = Componentes.objects.all()
	return render(request, template, locals())

def ver_informe(request, template='admin/ver_informe.html', pk=None):
	proyecto = get_object_or_404(DatosGenerales, id=pk)
	meses = CHOICES_MESES
	informe = RegistroPlanAnual.objects.filter(proyecto__id=pk)
	return render(request, template, locals())