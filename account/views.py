from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from video.models import Post


def registration_view(request):
    context={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form']=form
    else:
        form = RegistrationForm()
        context['registration_form']=form
    return render(request,'register.html',context)

def logoutview(request):
    logout(request)
    return redirect('/')



def loginview(request):
    
    context = {}
    user=request.user
    if user.is_authenticated:
        return redirect('/')
    
    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect('/')


    else:
        form= AccountAuthenticationForm

    context['loginform'] = form
    return render(request,'login.html',context)
                           

def must_authenticate_view(request):
    return render(request, 'must_authenticate.html',{})

def must_be_staff(request):
    return render(request, 'noright.html',{})