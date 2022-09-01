# Criando uma API REST

## Configuração inicial

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