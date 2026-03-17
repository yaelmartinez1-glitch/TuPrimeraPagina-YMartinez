from django.shortcuts import render
from .models import Post

def inicio(request):
    return render(request, "blog/inicio.html")

def buscar(request):
    return render(request, "blog/buscar.html")

def resultados(request):

    titulo = request.GET.get("titulo")

    posts = Post.objects.filter(titulo__icontains=titulo)

    return render(request, "blog/resultados.html", {"posts": posts})