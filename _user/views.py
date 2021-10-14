from django.contrib.auth import authenticate, login as log_in, logout
from django.http.response import HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from _user.forms import SignUpForm

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')

    if request.method == 'POST':
        fm_data = SignUpForm(request.POST)
        cfmd =  fm_data.cleaned_data
        print(cfmd)

        if fm_data.is_valid():
            fm_data.save()
            return HttpResponseRedirect('/profile/')
        else:
            if cfmd['password1'] != cfmd['password2']:
                messages.add_message(request, messages.ERROR, "Password didn't Match")
                return render(request, '_user/signup.html', {
                    'title': 'Error Occured !! ',
                    'signupform': SignUpForm()
                })
    return render(request, '_user/signup.html', {
        'title': 'Sign Up',
        'signupform': SignUpForm()
    })


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')

    if request.method == "POST":

        fm_data = AuthenticationForm(request=request, data=request.POST)

        if fm_data.is_valid():
            user = fm_data.cleaned_data['username']
            passw = fm_data.cleaned_data['password']
            USER = authenticate(username=user, password=passw)
            if USER is not None:
                log_in(request, USER)
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponseRedirect('/login/')

        else:
            messages.add_message(request, messages.)
            return redirect('login', msg=fm_data.cleaned_data)
            # return render(request, '_user/login.html', {
            #     'title':'!!!!!',
            #     'loginform':AuthenticationForm(),
            #     'msg':fm_data.cleaned_data["username"]
            # })
    else:
        return render(request, '_user/login.html', {
            'title': 'Log In',
            'loginform': AuthenticationForm()
        })


def profile(request):
    if request.method == 'POST':
        profile_data = UserChangeForm(request.POST)
        if profile_data.is_valid():
            profile_data.save()
        else:
            message.DANGER('request', )
            return render('/profile/')
    return render(request, '_user/profile.html', {
        'title': 'PROFILE__',
        'userchangeform':UserChangeForm()
    })


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
