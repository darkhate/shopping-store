from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import PostModel
from django.contrib.auth.decorators import login_required

def data_view(request):
	template = "test.html"
	qs = PostModel.objects.all()
	context = {
	"query_list":qs,
	}
	return render(request,template,context)

def data_detail_view(request ,id=None):
    obj = get_object_or_404(PostModel , id=id)
    context = {
	"object":obj,
	}
    template ="Detail.html"
    return render(request , template , context)

@login_required(login_url='/login/')
def login_view(request):
	print('456')
	qs = PostModel.objects.all() 
	context = {
	"query_list":qs,
	}
	print('123')
	if request.user.is_authenticated():
		template = "test.html"
	else:
		template = "log_in.html"
		return HttpResponseRedirect("/login")

	return render(request,template,context)