from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    # Criado uma constante de instância
    """
    Desta forma no Banco de dados será gravado apenas a letra inicial, porém o programa irá carregar toda a informação
    """
    NIVEL = (
        ('B', 'Básico'),
        ('I', "Intermediário"),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
    
    # __str define a forma com que a Classe será representada.
    def __str__(self):
        return self.descricao
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) # no "on_delete" o CASCADE é para caso o aluno for deletado a matricula também seja deletada 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')