from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import PostModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm

def Create_view(request):
	form = PostModelForm( request.POST or None)
	context = {
	       "form":form,
	}
	if form.is_valid():
	   #判斷資料是否存在
	   obj = form.save(commit=False)
	   #save() 接受一个可选的commit 关键字参数，其值为True 或False。如果save() 时commit=False，那么它将返回一个还没有保存到数据库的对象。这种情况下，你需要调用返回的模型实例的save()。 如果你想在保存之前自定义一些处理，或者你想使用特定的模型保存选项，可以这样使用。commit 默认为True。
       #使用commit=False 的另外一个副作用是在模型具有多对多关系的时候。如果模型具有多对多关系而且当你保存表单时指定commit=False，Django 不会立即为多对多关系保存表单数据。这是因为只有实例在数据库中存在时才可以保存实例的多对多数据。
	   obj.save()
	   messages.success(request , "Crete New View Success!!")
	   context = {
	       "form":PostModelForm( request.POST or None)
	   }

	template = "create_view.html"
	return render(request,template,context)	


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