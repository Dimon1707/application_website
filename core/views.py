from django.shortcuts import render


def index(reguest):
    '''
     Это функция отрисовки гл.страницы
    '''
    return render(reguest, 'index.html')
