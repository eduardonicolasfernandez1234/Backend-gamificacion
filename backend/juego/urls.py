from django.conf.urls import url
from django.urls import include
from rest_framework import routers


from juego.api import JuegoViewSet, ModoJuegoViewSet, NivelViewSet, PreguntaViewSet, OpcionPreguntaViewSet, LogroViewSet, \
    EstatusViewSet, CanjeoViewSet, ProductoCanjeoViewSet, PremioViewSet, ArticuloViewSet, ImagenPaginaViewSet, \
    DatoCuriosoViewSet, CategoriaPuzzleViewSet, ImagenPuzzleViewSet, SubImagenPuzzleViewSet

router = routers.DefaultRouter()
router.register(r'juego', JuegoViewSet)
router.register(r'modojuego', ModoJuegoViewSet)
router.register(r'nivel', NivelViewSet)
router.register(r'pregunta', PreguntaViewSet)
router.register(r'opcion-pregunta', OpcionPreguntaViewSet)
router.register(r'logro', LogroViewSet)
router.register(r'estatus', EstatusViewSet)
router.register(r'canjeo', CanjeoViewSet)
router.register(r'producto-canjeo', ProductoCanjeoViewSet)
router.register(r'premio', PremioViewSet)
router.register(r'articulo', ArticuloViewSet)
router.register(r'imagen-noticia', ImagenPaginaViewSet)
router.register(r'dato-curioso', DatoCuriosoViewSet)
router.register(r'categoria-puzzle', CategoriaPuzzleViewSet)
router.register(r'imagen-puzzle', ImagenPuzzleViewSet)
router.register(r'subimagen-puzzle', SubImagenPuzzleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
