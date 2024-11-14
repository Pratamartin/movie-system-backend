from rest_framework import viewsets
from .models import Usuario, Filme, Avaliacao, Discussao, ListaFilmes
from .serializers import UsuarioSerializer, FilmeSerializer, AvaliacaoSerializer, DiscussaoSerializer, ListaFilmesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class DiscussaoViewSet(viewsets.ModelViewSet):
    queryset = Discussao.objects.all()
    serializer_class = DiscussaoSerializer

class ListaFilmesViewSet(viewsets.ModelViewSet):
    queryset = ListaFilmes.objects.all()
    serializer_class = ListaFilmesSerializer
