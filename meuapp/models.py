from django.db import models
from django.core.validators import MinValueValidator 
from django.contrib.auth.models import User


# Create your models here.

class Movimento(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  nome = models.CharField(max_length=100)
  icone = models.CharField(max_length=10000)
  descricao = models.TextField(blank=True)
  tipo = models.CharField(max_length=60,
   choices={ 
   'Aquecimento': 'Aquecimento',
   'Acrobacia': 'Acrobacia',
   'Giro': 'Giro',
   'Outros': 'Outro Tipo'
   }
   ) 
  dificuldade =  models.IntegerField(
    validators=[ MinValueValidator(1) ]
  )
  realizados = models.BooleanField(default=False)
  
  def __str__(self):
    return self.nome

class Video(models.Model):
  nome = models.CharField(max_length=200)
  link =  models.URLField(max_length=2000) 
  movimento = models.ForeignKey(
    Movimento, 
   on_delete=models.CASCADE 
   ) 
  nomeConta = models.CharField(max_length=100)
  tempo = models.IntegerField()

  def __str__(self):
    return self.nome

