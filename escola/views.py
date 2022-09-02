from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializers import AlunoSerializer, CursoSerializer

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
    queryset = Curso.obects.all()
    serializer_class = CursoSerializer