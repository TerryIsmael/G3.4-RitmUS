from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserLoginForm, CreateIncidenceForm, CustomUserChangeForm, CustomUserChangePasswordForm, SetPasswordForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from base.models import  User, Incidence

def custom_login(request):
    data = {
        'form': CustomUserLoginForm()
    }
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            form.save()
            userAux = User.objects.filter(email=form.cleaned_data['email']).first()
            user = authenticate(
                username= userAux.username,
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, 'Logueado')
            return redirect(to='home')
        else:
            data['form'] = form
    return render(request, 'registration/login.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print(User.objects.filter(email=form.cleaned_data['email']).first())
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            print(form.cleaned_data['email'], form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Registrado correctamente')
            return redirect(to='home')
        else:
            data['form'] = form
    return render(request, 'registration/register.html', data)

@login_required
def change_user(request):
    user = request.user
    data = {
        'form': CustomUserChangeForm(initial={
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })
    }

    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario modificado correctamente')
            return redirect(to='home')
        else:
            data['form'] = form

    return render(request, 'registration/change_user.html', data)
@login_required
def change_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contraseña modificada correctamente')
            return redirect('home')
    else:
        form = SetPasswordForm(user=request.user)

    return render(request, 'registration/change_password.html', {'form': form})

@login_required
def create_incidence(request):
    data = {
        'form': CreateIncidenceForm(initial={'user': request.user})
    }
    if request.method == 'POST':
        form = CreateIncidenceForm(data=request.POST)
        if form.is_valid():
            incidence = form.save(commit=False)
            incidence.user = request.user
            incidence.save()
            form.save()
            messages.success(request, 'Incidencia creada correctamente')
            data['message'] = 'Incidencia creada correctamente'
            return redirect(to='list_incidences')
        else:
            data['form'] = form

    return render(request, 'incidences/newincidence.html', data)

@user_passes_test(lambda u: u.is_superuser, login_url='home')
def list_incidences(request):
    incidences = Incidence.objects.all() 
    data = {
        'incidences': incidences
    }
    return render(request, 'incidences/listincidence.html', data)

@login_required
def request_delete_account(request):
    if request.method == 'GET':
        return render(request, 'registration/delete_account.html')
    if request.method == 'POST':
        user=request.user
        user.is_active=False
        user.save()
        Incidence.objects.create(user=user,type="DELETE_ACCOUNT",description="El usuario ha solicitado borrar su cuenta")
        messages.success(request, 'Solicitud enviada correctamente')
        return redirect(to='home')
    
