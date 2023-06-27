from django.db import models

# Create your models here.

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=220)
    
    def __str__(self):
        return self.nome
    
    
class Livro(models.Model):
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=180)
    autores = models.TextField(null=True)
    total_paginas = models.IntegerField(default=0)
    data_pub = models.DateTimeField()
    preco = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    imagem = models.ImageField(upload_to="media", null=True, blank=True)
    
    def __str__(self):
        return self.titulo