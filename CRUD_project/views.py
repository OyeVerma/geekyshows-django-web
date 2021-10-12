from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import StudentRegistration as sr_m
from .forms import StudentRegistrationForm as sr_f
from django.http import HttpResponseRedirect

# Create your views here.


def index(request, msg=False):
    context = {
        'title': 'Add New Student',
        'form': sr_f(),
        'data': sr_m.objects.all()
    }
    if request.method == 'POST':
        sr_data = sr_f(request.POST)
        if sr_data.is_valid():
            sr_data.save()
            name = sr_data.cleaned_data['name']
            context.update({
                'title': 'Saved Successfully',
                'msg': f'Student ({name}) is Added Successfully'
            })
    return render(request, 'crud/index.html', context)



def delete(request, id):
    if request.method == 'POST':
        print('TRUE RTUT')
        delform = sr_m.objects.get(pk=id)
        delform.delete()
        return HttpResponseRedirect('/crud/add')
    else:
        return HttpResponse('404 Error.. Tried to Delete without post Request LOL')


def show_pass(request, id):
    if request.method == 'POST':
        student = sr_m.objects.get(pk=id)
        passed = student.passw
        return render(request, 'crud/index.html', {'passed': passed})
    else:
        return HttpResponse('Tried to gain pass Without post request LOL')


def update(request, id):
    if request.method == 'POST':
        old_data = sr_m.objects.get(pk=id)
        up_form = sr_f(request.POST, instance=old_data)
        if up_form.is_valid():
            up_form.save()
            return redirect('index')

        return render(request, 'crud/update.html', {
            'form': sr_f(instance=old_data),
            'data': old_data,
        })
    else:
        return HttpResponse('Update Error')
