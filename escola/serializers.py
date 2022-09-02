from pyexpat import model
from rest_framework import serializers
from escola.models import Aluno, Curso


'''
Criar uma classe para informa o modelo e campos a serem utilizados em cada serializers
class do tipo serializers modelo ModelSerializer - com isso transforma o modelo em outro tipo
'''
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # Outra forma de descriminar os campos a serem utilizados