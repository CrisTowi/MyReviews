from principal.models import Resena
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from principal.forms import ResenaForm

def inicio(request):

	if request.method == 'POST':
		formulario = ResenaForm(request.POST)
		if formulario.is_valid():
			return HttpResponseRedirect('/')

	else:
		formulario = ResenaForm()
	return render_to_response('inicio.html', {'formulario': formulario}, context_instance = RequestContext(request))