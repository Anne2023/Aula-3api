# Importando a classe 'serializers' do módulo 'rest_framework'
from rest_framework import serializers

# Importando o modelo de Subject do app
from ..models.subject import Subject

# Definindo a classe do serializador 'SubjectSerializer' que herda de 'serializers.ModelSerializer'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject # Especificando o 'model' associado ao serializador
        fields = '__all__' # Definindo que todos os campos do modelo serão incluídos no serializador