
from django.urls import path
from core.views import index, register, logout, application
from django.contrib.auth.views import LoginView

urlpatterns = [
    # 1-путь,2-функция,3-кр.название

    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('application/', application, name='application')


]
