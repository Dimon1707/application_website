
from django.shortcuts import render
from core.forms import UserRegistrationForm
from django.contrib.auth.views import auth_logout

def index(reguest):
    '''
     Это функция отрисовки гл.страницы
    '''
    return render(reguest, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'login.html', {'new_user': new_user})
    user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout(request):
    auth_logout(request)
    return render(request, 'application.html')

def application(request):
    if request.method == 'GET':

        return render(request, 'application.html' )

