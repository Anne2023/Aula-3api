# Importando classes necessárias do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos de Student e Task do app
from ..models.student import Student
from ..models.task import Task

# Importando o serializador TaskSerializer do app
from ..serializers.taskSerializer import TaskSerializer

# Definindo a classe da visualização 'StudentTasksView' que herda de 'APIView'
class StudentTasksView(APIView):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id) # Tenta obter um objeto Student com base no 'student_id' fornecido
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) # Se o Student não existe, retorna uma resposta "Não encontrado"
        
        tasks = Task.objects.filter(student=student) # Filtra as tarefas relacionadas ao estudante
        serializer = TaskSerializer(tasks, many=True) # Serializa as tarefas com many=True
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP