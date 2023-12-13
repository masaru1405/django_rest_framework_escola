from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('alunos', views.AlunoViewset, basename='Alunos')
router.register('cursos', views.CursoViewset, basename='Cursos')
router.register('matriculas', views.MatriculaViewset, basename='Matriculas')
