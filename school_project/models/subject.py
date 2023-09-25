# Importando a classe 'models' do módulo 'django.db'
from django.db import models

# Definindo a classe do modelo 'Subject' que herda de 'models.Model'
class Subject(models.Model):
    name = models.CharField(max_length=100) # Definindo um campo de caractere para o nome da disciplina com no máximo 100 caracteres   
    description = models.CharField(max_length=255) # Definindo um campo de caractere para a descrição da disciplina com no máximo 255 caracteres

    # Método '__str__' para retornar uma representação em string do objeto Subject
    def __str__(self):
        return self.name