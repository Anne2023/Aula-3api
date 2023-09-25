# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Student do app
from ..models.student import Student

# Definindo a classe do serializador 'StudentSerializer' que herda de 'serializers.ModelSerializer'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # Especificando o 'model' associado ao serializador
        fields = '__all__' # Definindo que todos os campos do modelo serão incluídos no serializador