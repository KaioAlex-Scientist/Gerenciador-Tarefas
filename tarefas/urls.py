from rest_framework.routers import DefaultRouter
from .views import TarefasViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefasViewSet)
urlpatterns = router.urls