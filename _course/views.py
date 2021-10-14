from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MainForm as fm, SearchForm as sfm, UserForm as ufm, inheritanceStudentForm, inheritanceTeacherForm
from .models import DbForm as dm, User
# Create your views here.


def index(request):

    if request.method == 'POST':
        data = dm.objects.all()
        # print(data)
        context = {
            'title': '-data-',
            'data': data
        }
    else:
        context = {
            'title': '__no_data__',
            'fm': fm(label_suffix=' + ')
        }

    return render(request, '_course/index.html', context)


def get_data_from_database(request):
    data = dm.objects.all()
    print(data)
    context = {
        'title': '_from_database_',
        'data': data
    }
    return render(request, '_course/get_data.html', context)


def search(request):
    if sfm(request.GET).is_valid() != True:
        context = {
            'title': '__writer_data__',
            'sfm': sfm()
        }
    else:
        sfmn = sfm(request.GET)
        if sfmn.is_valid():
            print(sfmn.is_valid())
            query = sfmn.cleaned_data['search']
            context = {
                'title': '__Got_data__',
                'data': dm.objects.get(pk=query)
                # 'data':'Sup Fuckers'
            }

    return render(request, '_course/search.html', context)


def save(request):
    if request.method == "POST":
        clean_fm = fm(request.POST)
        if clean_fm.is_valid():
            commit = dm(
                First_name=clean_fm.cleaned_data['first_name'],
                Last_name=clean_fm.cleaned_data['last_name'],
                Email=clean_fm.cleaned_data['email'],
                Phone=(clean_fm.cleaned_data['phone']),
                Password=clean_fm.cleaned_data['password']
            )
            commit.save()
        context = {
            'title': '__success__',
            'message': 'successfully Saved to Database',
            'firstname': clean_fm.cleaned_data['first_name']
        }
        return HttpResponseRedirect('/app/success/', context)
    else:
        context = {
            'title': '__success__',
            'fm': fm()
        }
        return render(request, '_course/save.html', context)


def success(request):
    return render(request, '_course/success.html')


def form(request):

    if request.method == 'POST':
        nfm = fm(request.POST)
        if nfm.is_valid():
            context = {
                'data': nfm.cleaned_data
            }
        else:
            context = {
                'data': 'Not Valid'
            }
    else:
        print('hltooo')
        context = {
            'fm': fm()
        }

    return render(request, '_course/form_validation.html', context)


def user(request):
    context = {
        'title':'__NEW__USER__',
        'ufm':ufm()
    }
    if request.method == 'POST':
        new = User()
        ufmn = ufm(request.POST, instance=new)
        if ufmn.is_valid():
            ufmn.save()

            context.update({'title':'__SUCCESS__'})

    return render(request, '_course/user.html', context)

import math
def proj_u_theta(request, u, theta):
    g = 9.81
    angle = math.radians(theta)
    usin, ucos = u*(math.sin(angle)), u*(math.cos(angle))
    print(usin, ucos)
    time = 2*(usin / g)
    range = ucos * time
    height = math.pow(usin, 2) / (2 * g)

    context = {
        'u':u,
        'angle':[f'{theta}_deg', f'{angle}_rad'],
        't':time,
        'r':range,
        'h':height,

    }

    return render(request, '_course/projectile.html', context)

def stureg(request):
    return render(request, '_course/stureg.html', {
        'title':'Student Registration',
        'form':inheritanceStudentForm()
    })

def teareg(request):
    return render(request, '_course/teareg.html', {
        'title':'Teacher Registration',
        'form':inheritanceTeacherForm()
    })


