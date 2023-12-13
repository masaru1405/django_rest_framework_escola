from rest_framework import viewsets

from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunoViewset(viewsets.ModelViewSet):
   """
   Exibindo todos os alunos(as)
   """    
   queryset = Aluno.objects.all() #consulta
   serializer_class = AlunoSerializer #faz a serialização


class CursoViewset(viewsets.ModelViewSet):
   """
   Exibindo todos os cursos
   """
   queryset = Curso.objects.all()
   serializer_class = CursoSerializer


class MatriculaViewset(viewsets.ModelViewSet):
   """
   Exibindo todas as matrículas
   """
   queryset = Matricula.objects.all()
   serializer_class = MatriculaSerializer