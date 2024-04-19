from django.contrib import admin
from .models import Movimento, Video

# Register your models here.

class MovimentoAdmin (admin.ModelAdmin):
  list_display = ['nome', 'tipo', 'dificuldade', 'realizados'] 
  ordering = ['dificuldade']

admin.site.register(Movimento, MovimentoAdmin)

class VideoAdmin (admin.ModelAdmin):
  list_display = ['nome', 'link', 'movimento', 'tempo'] 
  ordering = ['tempo']

admin.site.register(Video, VideoAdmin)

