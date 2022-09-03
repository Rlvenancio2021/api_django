# Criando uma API REST

## API Referente para gestão de dados de uma escola com dados de Alunos, Cursos e Matriculas realizadas

### Tecnologias que estou me dedicando atualmente
<div style="display: inline_block"><br/>
  <img aling="center" alt="Python3" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img aling="center" alt="Django3" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img aling="center" alt="MySQL" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white"/>
</div>

### Objetivo do Projeto

Adminstrar Banco de Dados de uma escola com controle dos dados de Alunos e Cursos, por meio da página Admin do Framework Django, possibilitando a uso do CRUD de uma forma mais amigavel ao usuário.

Foi adicionado uma camada de proteção de autenticação básica para que os usuários tenham acesso ao conteúdo da API.


### Saída de Dados

Os dados de saída são no formato JSON e o banco de dados utilizado é o MySQL


### Configuração inicial

1. Criar um ambiente virtual para melhor controle dos pacotes e bibliotecas a serem instaladas para o projeto.
Comandos MAC ou Linux
```
python3 -m venv ./venv
```

2. Ativar ambiente virtual
```
$ source venv/bin/activate
// Para desativar
$ deactivate
```
3. Instalar Framework DJANGO
```
pip install Django==3.0.7
```
4. Inicia um projeto no Django, configurar linguagem e fuso-horário
```
django-admin startproject setup . //"setup" é o nome do app a ser criado
// Em setup/settings.py alterar as variáveis conforme abaixo
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

## Cria APP do projeto que será responsável pelos dados do programa

Rodar o comando 

```
python manage.py startapp <nome_do_app>
```


## Instala Django REST

*Antes* de realizar as instalações verificar se o *ambiente virtual está ativado*.

Django Rest Framework cadastra URLs, e serializa os dados recebidos do banco de dados para JSON
Markdown é o suporte para o browsable API

```
pip install djangorestframework
pip install markdown
```

## Criar os modelos de banco de dados

Para criação dos modelos de banco de dados será necessário realizar as seguintes alterações.

 - Na pasta do APP criado em *models* criar as Classes com a estrutura que irá ser utilizada no banco de dados, após finalizados rodar o comando abaixo para criar as migrações para o banco de dados

 ```
 python manage.py makemigrations
 ```

Verificar se já esta configurada a coneção com o banco de dados escolhido. Caso contrário:
 - Banco de Dados MySQL
 	1. pip install mysqlclient

 Por fim rodar o comando 

 ```
 python manage.py migrate
 ``` 
