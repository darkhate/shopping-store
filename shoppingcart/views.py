from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def data_view(request):
    qs = PostModel.objects.all()
    print(qs)
    return HttpResponse(qs)

def render_where(request):
	path = 'test.html'
	qs = PostModel.objects.all()
	context = {
	"query_list":qs,
	}
	return render(request,path,context)