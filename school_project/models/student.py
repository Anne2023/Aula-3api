# Importando a classe 'models' do módulo 'django.db'
from django.db import models
from .task import Task

# Definindo a classe do modelo 'Student' que herda de 'models.Model'
class Student(models.Model):
    name = models.CharField(max_length=100) # Definindo um campo de caractere para o nome do estudante com no máximo 100 caracteres
    email = models.EmailField(max_length=100) # Definindo um campo de email para o email do estudante com no máximo 100 caracteres

    # Método '__str__' para retornar uma representação em string do objeto Student
    def __str__(self):
        return self.name