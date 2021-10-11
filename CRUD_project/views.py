from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import StudentRegistration as sr_m
from .forms import StudentRegistrationForm as sr_f
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(request, message=False):
    context ={
            'title':'Add New Student',
            'form':sr_f(),
            'data':sr_m.objects.all()
        }
    if request.method == 'POST':
        sr_data = sr_f(request.POST)
        if sr_data.is_valid():
            sr_data.save()
            name = sr_data.cleaned_data['name']
            context.update({
                'title':'Saved Successfully',
                
                'message':f'Student ({name}) is Added Successfully'
            })
    return render(request, 'crud/add_show.html', context)

def index(request):
    return render(request, 'crud/index.html')

def delete(request, id):
    if request.method == 'POST':
        print('TRUE RTUT')
        delform = sr_m.objects.get(pk=id)
        delform.delete()
        return HttpResponseRedirect('crud/add')
    else:
        return HttpResponse('404 Error')
