from django.shortcuts import render, redirect
from .models import Movimento, Video
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

@login_required
def caminhada(request):
  ranking ={
      'nome': 'Caminhada',
      'icone': 'Caminhada.jpg',
      'descricao': 'A caminhada no pole dance é essencial para movimentos fluidos e transições elegantes ao redor da barra.',
      'links': [
          {'url': "https://youtu.be/vogipXxQqBM?si=VxzetgLpY7fG0mEx", 'descricao': 'Tutorial 1'},
          {'url': "https://youtu.be/E5uZlZCJ31I?si=dwX1udLaR2PTkCdO", 'descricao': 'Tutorial 2'}
      ]
  }

  return render(request, 'caminhada.html', {'ranking': ranking})

@login_required
def travasBasicas(request):
  ranking = [
    {
        'nome': 'Travas básicas',
        'descricao': 'As travas básicas são fundamentais para garantir segurança e estabilidade ao segurar a barra durante os movimentos.',
        'subcategorias': [
            {'nome': 'Abdominal Trava 1', 'icone': 'Trava.jpg'},
            {'nome': 'Abdominal Trava P', 'icone': 'TravaP.jpg'},
            {'nome': 'Abdominal Trava Reta', 'icone': 'TravaReta.jpg'}
        ],
        'links': [
            {'url': "https://youtube.com/shorts/zsibX1PuLL8?si=tkXE6Cdsa1C2jg8b", 'descricao': 'Abdominal Trava P'},
            {'url': "https://youtube.com/shorts/xD1PyPkvX1k?si=MzY71mt3TVhyOm6U", 'descricao': 'Abdominal Trava Reta'}
        ]
    }
  ]
  return render(request, 'travasBasicas.html', {'ranking': ranking})

@login_required
def jump (request):
  ranking = [
    {
        'nome': 'Jump',
        'icone': 'jump.jpg',
        'descricao': 'O jump, que envolve pular e se segurar na barra com as pernas, adiciona dinamismo e impacto às apresentações.',
        'links': [
            {'url': "https://youtu.be/wZt7IBUwEm4?si=QN41pIKl84bV3oqh", 'descricao': 'Tutorial 1'},
            {'url': "https://youtu.be/ov5HbxiJKPk?si=Z4rerep_7IiK3SXm", 'descricao': 'Tutorial 2'}
        ]
    }
  ]

  return render(request, 'jump.html', {'ranking': ranking})

@login_required
def compasso (request):
  ranking = [
    {
        'nome': 'Compasso',
        'icone': 'compasso.jpg',
        'descricao': 'O compasso é uma série de movimentos ritmados ao redor da barra, contribuindo para expressão e fluidez nas performances.',
        'links': [
            {'url': "https://youtu.be/fhuEWq3dueo?si=cQaEhdgTyKprrjxO", 'descricao': 'Tutorial 1'},
            {'url': "https://youtu.be/FTly5gulwOw?si=_3s6uRsG3gpsd6VP", 'descricao': 'Tutorial 2'}
        ]
    }
  ]

  return render(request, 'compasso.html', {'ranking': ranking})
  
@login_required
def subida (request):
  ranking = [
    {
          'nome': 'Subida',
          'icone': 'Subida.jpg',
          'descricao': 'A subida é um movimento que demonstra força e habilidade, permitindo escalar a barra de forma graciosa.',
          'links': [
              {'url': "https://youtu.be/I0ADcdaEwOU?si=zdqrnX65TaxWGdav", 'descricao': 'Subida Iguana'},
              {'url': "https://youtu.be/g8hzhG9WmJ0?si=4Oj8P1f_5FbgY3XI", 'descricao': 'Subida Caterpilar'}
          ]
      }
    ]

  return render(request, 'subida.html', {'ranking': ranking})

@login_required
def index(request):
  movimentos = Movimento.objects.filter(usuario=request.user).all()
  videos = Video.objects.all()
  
  return render(request, 'index.html', { 'nome':'Camilla Qiu', 'movimentos': movimentos, 'videos': videos })

@login_required
def create_movimentos(request):
  if request.method == "POST":
      nome = request.POST.get("nome")
      descricao = request.POST.get("descricao")
      tipo = request.POST.get("tipo")
      dificuldade = request.POST.get("dificuldade")
      realizados = request.POST.get("realizados")

      if nome and descricao and tipo and dificuldade:
          Movimento.objects.create(
              nome=nome,
              descricao=descricao,
              tipo=tipo,
              dificuldade=dificuldade,
              usuario=request.user
          )
          return redirect("home")
      else:
          return render(request, "erro.html", context={"message": "Todos os campos <mark><ins> marcados</mark></ins> são obrigatórios"})

  return render(request, "forms.html", context={"action": "Adicionar"})

@login_required
def update_movimentos(request, id):
  movimento = Movimento.objects.get(id=id)
  if request.method == "POST":
      nome = request.POST["nome"]
      descricao = request.POST["descricao"]
      tipo = request.POST["tipo"]
      dificuldade = request.POST["dificuldade"]
      realizados_value = request.POST.get("realizados")

      if nome and descricao and tipo and dificuldade:
          movimento.nome = nome
          movimento.descricao = descricao
          movimento.tipo = tipo
          movimento.dificuldade = dificuldade
          movimento.realizados = realizados_value == "on"
          movimento.save()
          return redirect("home")
      else:
        message = "Todos os campos <mark><ins> marcados</mark></ins> são obrigatórios"
        return render(request, "erro.html", context={"message": message, "action": "Editar", "movimento": movimento})

  return render(request, "forms.html", context={"action": "Editar", "movimento": movimento})

@login_required
def delete_movimentos(request,id):
  movimento = Movimento.objects.get(id = id)
  if request.method == "POST":
    if request.POST["confirm"]:
      movimento.delete()
      return redirect("home")

  return render(request, "are_you_sure.html", context={ "movimento": movimento})

def inicio(request):
  return render (request, 'inicio.html')

def login_usuario(request):
 formulario = AuthenticationForm()
 if request.method == 'POST' and request.POST:
  formulario = AuthenticationForm(request, request.POST)
  if formulario.is_valid():
    usuario = formulario.get_user()
    login(request, usuario)
    return redirect('/home')
 return render(request, 'login.html', {'formulario': formulario})

def cadastro_usuario(request):
 formulario = NovoUsuarioForm()
 if request.method == 'POST' and request.POST:
  formulario = NovoUsuarioForm(request.POST)
  if formulario.is_valid():
    novo_usuario = formulario.save(commit=False)
    novo_usuario.email = formulario.cleaned_data['email']
    novo_usuario.first_name = formulario.cleaned_data['first_name']
    novo_usuario.last_name = formulario.cleaned_data['last_name']
    novo_usuario.save()
    return redirect('/login')
 return render(request,'cadastro_usuario.html',
 {'formulario': formulario})


def logout_usuario(request):
  logout(request)
  return redirect('/')
