# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo Student e o serializador StudentSerializer do app
from ..models.student import Student
from ..serializers.studentSerializer import StudentSerializer

# Definindo a classe de visualização 'StudentListCreateView' que herda de 'APIView'
class StudentListCreateView(APIView):
    def get(self, request):
        students = Student.objects.all() # Obtém todos os estudantes do banco de dados
        serializer = StudentSerializer(students, many=True) # Serializa a lista de estudantes
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def post(self, request):
        serializer = StudentSerializer(data=request.data) # Serializa os dados recebidos na requisição
        if serializer.is_valid(): # Verifica se os dados são válidos
            serializer.save() # Salva o objeto Student no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se inválidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

# Definindo a classe de visualização 'StudentDetailView' que herda de 'APIView'
class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk) # Tenta obter um objeto Student com base no primary-key fornecido
        except Student.DoesNotExist:
            raise Http404 # Se o Student não existe, levanta uma exceção Http404 "não encontrado"

    def get(self, request, pk):
        student = self.get_object(pk) # Obtém o objeto Student com base na primary-key
        serializer = StudentSerializer(student) # Serializa o objeto Student
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def put(self, request, pk):
        student = self.get_object(pk) # Obtém o objeto Student com base na primary-key
        serializer = StudentSerializer(student, data=request.data) # Serializa os dados recebidos na requisição e associa-os ao objeto Student
        
        if serializer.is_valid(): # Verifica se os dados são válidos
            serializer.save() # Salva as alterações no objeto Student no banco de dados
            return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se inválidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

    def delete(self, request, pk):
        student = self.get_object(pk) # Obtém o objeto Student com base na primary-key
        student.delete() # Exclui o objeto Student do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído