from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=40)