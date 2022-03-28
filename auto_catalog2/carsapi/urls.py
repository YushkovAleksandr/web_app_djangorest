from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', views.CarViewSet),
router.register(r'popular', views.CarPopularViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cars/', views.CarListView.as_view()),
    path('popular/', views.CarPopularView.as_view()),
    path('post_car/', views.CarCreateView.as_view())
]
