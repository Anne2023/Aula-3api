# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos Student e Task e o serializador TaskSerializer do seu aplicativo (assumindo que existem)
from ..models.student import Student
from ..models.task import Task
from ..serializers.taskSerializer import TaskSerializer

# Definindo a classe de visualização 'TaskListCreateView' que herda de 'APIView'
class TaskListCreateView(APIView):
    def get(self, request):
        tasks = Task.objects.all() # Obtém todas as tarefas do banco de dados
        serializer = TaskSerializer(tasks, many=True) # Serializa a lista de tarefas
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def post(self, request):
        serializer = TaskSerializer(data=request.data) # Serializa os dados recebidos na requisição
        if serializer.is_valid(): # Verifica se os dados são válidos
            serializer.save() # Salva o objeto Task no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se inválidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

# Definindo a classe de visualização 'TaskDetailView' que herda de 'APIView'
class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk) # Tenta obter um objeto Task com base na primary-key fornecida
        except Task.DoesNotExist:
            raise Http404 # Se o Task não existe, levanta uma exceção Http404

    def get(self, request, pk):
        task = self.get_object(pk) # Obtém o objeto Task com base na primary-key
        serializer = TaskSerializer(task) # Serializa o objeto Task
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def put(self, request, pk):
        task = self.get_object(pk) # Obtém o objeto Task com base na primary-key
        serializer = TaskSerializer(task, data=request.data) # Serializa os dados recebidos na requisição e associa-os ao objeto Task
        
        if serializer.is_valid(): # Verifica se os dados são válidos
            serializer.save() # Salva as alterações no objeto Task no banco de dados
            return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

    def delete(self, request, pk):
        task = self.get_object(pk) # Obtém o objeto Task com base na primary-key
        task.delete() # Exclui o objeto Task do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído