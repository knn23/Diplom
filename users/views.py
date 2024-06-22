from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = "Не вдалося зареєструватися. Будь ласка, перевірте введені дані."

            # Проверка возможных ошибок формы и добавление сообщений об ошибках к общему сообщению
            if 'username' in form.errors:
                error_message += " " + form.errors['username'][0]  # Ошибка имени пользователя
            if 'email' in form.errors:
                error_message += " " + form.errors['email'][0]  # Ошибка электронной почты
            if 'password1' in form.errors:
                error_message += " " + form.errors['password1'][0]  # Ошибка пароля
            if 'password2' in form.errors:
                error_message += " " + form.errors['password2'][0]  # Ошибка подтверждения пароля

            return render(request, 'users/register.html', {'form': form, 'error': error_message})
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')



def home(request):
    return render(request, 'users/home.html')

