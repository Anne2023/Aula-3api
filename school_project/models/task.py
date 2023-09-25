# Importando a classe 'models' do módulo 'django.db'
from django.db import models


# Definindo a classe do modelo 'Task' que herda de 'models.Model'
class Task(models.Model):
    title = models.CharField(max_length=100) # Definindo um campo de caractere para o título da tarefa com no máximo 100 caracteres
    description = models.TextField() # Definindo um campo de texto para a descrição da tarefa
    delivery_date = models.DateField() # Definindo um campo de data para a data de entrega da tarefa
    completed = models.BooleanField(default=False) # Definindo um campo booleano para indicar se a tarefa foi concluída ou não, com valor padrão False
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='student_tasks') # Definindo um relacionamento many-to-one de chave estrangeira com o modelo Student
    subjects = models.ManyToManyField('Subject', related_name='tasks') # Definindo um relacionamento many-to-many com o modelo Subject
  
    # Método '__str__' para retornar uma representação em string do objeto Task
    def __str__(self):
        return self.title