# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Task do app
from school_project.models import Task


# Definindo a classe do serializador 'TaskSerializer' que herda de 'serializers.ModelSerializer'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # Especificando o 'model' associado ao serializador
        fields = '__all__' # Definindo que todos os campos do modelo serão incluídos no serializador