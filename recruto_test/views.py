from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def greet(request):
    # Получаем параметры из GET-запроса
    name = request.GET.get('name')
    message = request.GET.get('message')

    # Формируем ответ
    if name and message:
        response = f"<h1>Hello {name}! {message}!</h1>"
    else:
        response = "Введите параметры name и message в адресной строке"
    return HttpResponse(response)
