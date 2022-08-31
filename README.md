# Criando uma API REST

## Configuração inicial

1. Criar um ambiente virtual para melhor controle dos pacotes e bibliotecas a serem instaladas para o projeto.
Comandos MAC ou Linux
```
python3 -m venv ./venv
```

2. Ativar ambiente virtual
```
source venv/bin/activate
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
