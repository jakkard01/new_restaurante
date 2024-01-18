# mi_restaurante/views.py

from django.shortcuts import render

def inicio(request):
    return render(request, 'mi_restaurante/inicio.html')
