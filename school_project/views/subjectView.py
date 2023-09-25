# Importando classes necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo Subject e o serializador SubjectSerializer do seu aplicativo (assumindo que existem)
from school_project.models.subject import Subject
from school_project.serializers.subjectSerializer import SubjectSerializer


# Definindo a classe de visualização 'SubjectListCreateView' que herda de 'APIView'
class SubjectListCreateView(APIView):
    def get(self, request):
        subjects = Subject.objects.all() # Obtém todas as disciplinas do banco de dados
        serializer = SubjectSerializer(subjects, many=True) # Serializa a lista de disciplinas
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def post(self, request):
        serializer = SubjectSerializer(data=request.data) # Serializa os dados recebidos na requisição
        
        if serializer.is_valid(): # Verifica se os dados são válidos
            serializer.save() # Salva o objeto Subject no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna os dados serializados em uma resposta HTTP com status 201 (Created)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

# Definindo a classe de visualização 'SubjectDetailView' que herda de 'APIView'
class SubjectDetailView(APIView):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk) # Tenta obter um objeto Subject com base na primary-key fornecida
        except Subject.DoesNotExist:
            raise Http404 # Se o Subject não existe, levanta uma exceção Http404

    def get(self, request, pk):
        subject = self.get_object(pk) # Obtém o objeto Subject com base na primary-key
        serializer = SubjectSerializer(subject) # Serializa o objeto Subject
        return Response(serializer.data) # Retorna os dados serializados em uma resposta HTTP

    def put(self, request, pk):
        subject = self.get_object(pk) # Obtém o objeto Subject com base na primary-key
        serializer = SubjectSerializer(subject, data=request.data) # Serializa os dados recebidos na requisição e associa-os ao objeto Subject
        
        if serializer.is_valid():# Verifica se os dados são válidos
            serializer.save()# Salva as alterações no objeto Subject no banco de dados
            return Response(serializer.data)# Retorna os dados serializados em uma resposta HTTP
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se os dados não forem válidos, retorna os erros em uma resposta HTTP com status 400 (Bad Request)

    def delete(self, request, pk):
        subject = self.get_object(pk) # Obtém o objeto Subject com base na primary-key
        subject.delete() # Exclui o objeto Subject do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna uma resposta HTTP com status 204 (No Content) indicando que o objeto foi excluído