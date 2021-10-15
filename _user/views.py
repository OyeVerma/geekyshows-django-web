from django.contrib.auth import authenticate, login as log_in, logout
from django.http.response import HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

from _user.forms import SignUpForm, LogInForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        fm_data = UserCreationForm(request.POST)
        print('\n'*10, fm_data, '\n'*10)
        if fm_data.is_valid():
            fm_data.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Form Submitted'
            )
            return HttpResponseRedirect('/profile/')
        else:
            # if 
            return render(
                request,
                '_user/signup.html',
                {
                    'signupform': UserCreationForm(request.POST)
                }
            )

    return render(
        request,
        '_user/signup.html',
        {
            'signupform': UserCreationForm()
        }
    )


def login(request):
    if request.user.is_authenticated:
        print(1)
        return HttpResponseRedirect('/profile/')

    if request.method == "POST":

        fm_data = LogInForm(request=request, data=request.POST)

        if fm_data.is_valid():
            print(2)
            user = fm_data.cleaned_data['username']
            passw = fm_data.cleaned_data['password']
            USER = authenticate(username=user, password=passw)
            if USER is not None:
                print(2)
                log_in(request, USER)
                return HttpResponseRedirect('/profile/')
            else:
                print(3)
                messages.add_message(request, messages.ERROR, 'user is NONE')
                return HttpResponseRedirect('/login/')

        else:
            print(4)
            messages.add_message(request, messages.ERROR, fm_data.cleaned_data)
            return redirect('login')
            # return render(request, '_user/login.html', {
            #     'title':'!!!!!',
            #     'loginform':AuthenticationForm(),
            #     'msg':fm_data.cleaned_data["username"]
            # })
    else:
        print(5)
        return render(request, '_user/login.html', {
            'title': 'Log In',
            'loginform': LogInForm()
        })


def profile(request):
    if request.method == 'POST':
        profile_data = UserChangeForm(request.POST)
        if profile_data.is_valid():
            profile_data.save()
        else:
            messages.add_message(request, messages.DANGER,
                                 'Form Field are NOt valid')
            return render('/profile/')
    
    if not request.user.is_authenticated:
        return render(request, '_user/profile.html', {
        'title': '__PROFILE__',
        'userchangeform': UserChangeForm()
    })

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')

def pass_change(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            pass_data = PasswordChangeForm(user=request.user, date=request.POST)
            if pass_data.is_valid:
                pass_data.save()
                return HttpResponseRedirect('/profile/')
        else:
            return render(
                request,
                '_user/passchange.html',
                {
                    'title':'Change Password',
                    'passform':PasswordChangeForm(user=request.user)
                }
            )
    else:
        return redirect('signup')