# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render_to_response

def homepage(request):

	from django.conf import settings
	context = {'MEDIA_URL': settings.MEDIA_URL}
	#return HttpResponse('Bem-Vindo ao Eventex')
	return render_to_response('index.html', context)
