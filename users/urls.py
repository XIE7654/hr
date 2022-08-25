from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserLogin

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLogin.as_view()),
]