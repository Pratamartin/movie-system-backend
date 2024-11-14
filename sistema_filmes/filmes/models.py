from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=50, choices=[
        ('Cinéfilo', 'Cinéfilo'),
        ('Usuário Casual', 'Usuário Casual'),
        ('Pai/Mãe', 'Pai/Mãe'),
        ('Estudante de Cinema', 'Estudante de Cinema'),
        ('Apreciador de Séries', 'Apreciador de Séries')
    ])
    avatar = models.CharField(max_length=255, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)
    conta_verificada = models.BooleanField(default=False)

class PerfilPreferencias(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    generos_preferidos = models.JSONField()
    diretores_preferidos = models.JSONField()
    atores_preferidos = models.JSONField()
    restricoes_conteudo = models.CharField(max_length=50, null=True, blank=True)

class Diretor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    pais_origem = models.CharField(max_length=100, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

class Ator(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    pais_origem = models.CharField(max_length=100, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.SET_NULL, null=True, blank=True)
    duracao = models.IntegerField(null=True, blank=True)
    genero = models.JSONField()  # armazenar os gêneros como lista JSON
    sinopse = models.TextField(null=True, blank=True)
    avaliacao_media = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    url_poster = models.CharField(max_length=255, null=True, blank=True)
    data_adicao = models.DateTimeField(auto_now_add=True)
    elenco = models.ManyToManyField(Ator, through='Elenco')

class Elenco(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='elenco_filmes')
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)

class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

class Discussao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    topico_discussao = models.CharField(max_length=255)
    comentario = models.TextField(null=True, blank=True)
    data_comentario = models.DateTimeField(auto_now_add=True)

class ListaFilmes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    tipo_lista = models.CharField(max_length=20, choices=[
        ('Para Assistir', 'Para Assistir'),
        ('Assistido', 'Assistido')
    ])

class HistoricoVisualizacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_visualizacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Assistido', 'Assistido'),
        ('Pausado', 'Pausado')
    ])

class Sugestao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    origem_recomendacao = models.CharField(max_length=255, null=True, blank=True)
    data_sugestao = models.DateTimeField(auto_now_add=True)

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    tipo_notificacao = models.CharField(max_length=50, choices=[
        ('novo filme', 'novo filme'),
        ('atualização de catálogo', 'atualização de catálogo')
    ])
    status = models.CharField(max_length=20, choices=[
        ('lida', 'lida'),
        ('não lida', 'não lida')
    ], default='não lida')
    data_notificacao = models.DateTimeField(auto_now_add=True)

class ConfiguracoesConta(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    preferencia_idioma = models.CharField(max_length=50, null=True, blank=True)
    notificacoes_ativadas = models.BooleanField(default=True)
    preferencia_tema = models.CharField(max_length=10, choices=[
        ('claro', 'claro'),
        ('escuro', 'escuro')
    ], default='claro')
