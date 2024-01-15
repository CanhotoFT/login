from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_Length=225)
    idade = models.IntegerField()
