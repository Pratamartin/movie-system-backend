from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, FilmeViewSet, AvaliacaoViewSet, DiscussaoViewSet, ListaFilmesViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'filmes', FilmeViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'discussoes', DiscussaoViewSet)
router.register(r'lista_filmes', ListaFilmesViewSet)

urlpatterns = router.urls
