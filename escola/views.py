from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer

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
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno ou aluna"""
    # Função para filter no banco de dados o aluno que foi passado na requisição.
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer