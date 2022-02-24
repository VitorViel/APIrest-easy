from django.urls import path

from rest_framework.routers import DefaultRouter

from app.views import TodoViewSet
# from app.views import TodoListandCreate, TodoListUpdateandDelete

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('', TodoListandCreate.as_view()),
#     path('<int:pk>/', TodoListUpdateandDelete.as_view())
# ]
