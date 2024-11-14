from rest_framework import serializers
from .models import Usuario, Filme, Avaliacao, Discussao, ListaFilmes

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class DiscussaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussao
        fields = '__all__'

class ListaFilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaFilmes
        fields = '__all__'
