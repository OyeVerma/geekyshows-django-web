from django.contrib.auth import authenticate, login as log_in, logout, update_session_auth_hash
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

from _user.forms import SignUpForm, LogInForm, DetailsChangeForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, '_user/home.html', {
            'title':'__Home__',
        })
    else:
        return redirect('signup')

def signup(request):
    if request.method == 'POST':
        fm_data = UserCreationForm(request.POST)
        if fm_data.is_valid():
            fm_data.save()
            messages.add_message(request, messages.SUCCESS, 'Signed Up Successfully !!')
            user = fm_data.cleaned_data['username']
            passw = fm_data.cleaned_data['password1']
            USER = authenticate(username=user, password=passw)
            if USER is not None:
                log_in(request, USER)
                messages.add_message(request, messages.SUCCESS, 'Logged In Successfully !!')
                return redirect('home')
        else:
            # if 
            messages.add_message(request, messages.ERROR, 'Invalid Form !')
            return render(request, '_user/signup.html', {
                'form': UserCreationForm(request.POST)
                })
    else:
        return render(request, '_user/signup.html', {
            'form':UserCreationForm()
        })

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.method == "POST":

        fm_data = LogInForm(request=request, data=request.POST)

        if fm_data.is_valid():
            user = fm_data.cleaned_data['username']
            passw = fm_data.cleaned_data['password']
            USER = authenticate(username=user, password=passw)
            if USER is not None:
                log_in(request, USER)
                messages.add_message(request, messages.SUCCESS, 'Logged In Successfully !!')
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'user is NONE')
                return HttpResponseRedirect('/login/')

        else:
            messages.add_message(request, messages.ERROR, 'form is not valid')
            return redirect('login')
            # return render(request, '_user/login.html', {
            #     'title':'!!!!!',
            #     'loginform':AuthenticationForm(),
            #     'msg':fm_data.cleaned_data["username"]
            # })
    else:
        return render(request, '_user/login.html', {
            'title': 'Log In',
            'form': LogInForm()
        })

def changedetails(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            changedetails_data = DetailsChangeForm(request.POST, instance=request.user)
            if changedetails_data.is_valid():
                changedetails_data.save()
                messages.add_message(request, messages.SUCCESS, 'Credentials Saved SuccessFully')
                return HttpResponseRedirect('/home/')
            else:
                messages.add_message(request, messages.WARNING, 'Form Field are NOt valid')
                return redirect('changedetails')        
        else:
            return render(request, '_user/changedetails.html', {
                'form':DetailsChangeForm(initial={
                    'username':request.user.username,
                    'first_name':request.user.first_name,
                    'last_name':request.user.last_name,
                    'email':request.user.email,
                }),

        })

    else:
        messages.add_message(request, messages.INFO, 'You Have to SIGNUP first')
        return redirect('signup')

def logout_user(request):
    if request.user.is_authenticated:
        # messages.SUCCESS(request, f'User {request.user}, Logged out Successfully')
        messages.add_message(request, messages.INFO, f'User ``{request.user}``, Logged out Successfully')
        logout(request)
        return HttpResponseRedirect('/login/')

def pass_change(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            pass_data = PasswordChangeForm(user=request.user, data=request.POST)
            if pass_data.is_valid():
                pass_data.save()
                update_session_auth_hash(request, user=request.user)
                messages.add_message(request, messages.SUCCESS, 'Password Changed Successfully')
                return redirect('home')
        
        else:
            return render(request, '_user/passchange.html', {
                'title':'Change Your PassWord',
                'form':PasswordChangeForm(user=request.user)
            })
    
    return redirect('login')
    #         else:
    #             messages.add_message(request, messages.WARNING, 'Form NOt Valid')
    #             return render(request, '_user/passchange.html',{
    #                     'title':'Change Password 2',
    #                     'passform':PasswordChangeForm(user=request.user)
    #                 })
    #     else:
    #         return render(
    #             request,
    #             '_user/passchange.html',
    #             {
    #                 'title':'Change Password 1',
    #                 'passform':PasswordChangeForm(user=request.user)
    #             }
    #         )
    # else:
    #     return redirect('signup')
