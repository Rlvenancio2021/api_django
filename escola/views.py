from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

'''
A estrutura Rest permite incluir uma abstração para lidar com "VIEWSET",
que permite pensar na modelagem de negócio e como a aplicação esta se desenvolvendo.
'''

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer