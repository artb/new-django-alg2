from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register('calculo', viewsets.CalculoViewSet)


urlpatterns = router.urls
