from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

#def Home(request):
#	return HttpResponse("<!DOCTYPE html><html><head><style>h1 {color:blue;}</style></head><body><h1>Hello!!</h1></body></html>")

def Home(request):
	response = HttpResponse(content_type='application/json')
	response = HttpResponse(content_type='text/html')
	response.content="<!DOCTYPE html><html><head><style>h1 {color:blue;}</style></head><body><h1>Hello!!</h1></body></html>"
	response.write('456')
	response.code_status=200
	return response

def redirect_where(request):
	return HttpResponseRedirect("/some/path/")


