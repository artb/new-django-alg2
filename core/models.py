from django.db import models


# Create your models here.

class Calculo(models.Model):
    matriz = models.CharField()
    determinante = models.BooleanField()
    traco = models.BooleanField()
    transposta = models.BooleanField()
    inversa = models.BooleanField()
    polinomio_caracteristico = models.BooleanField()
    autovalores = models.BooleanField()
    autovetores = models.BooleanField()
    matriz_diagonal = models.BooleanField()