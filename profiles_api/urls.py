from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, UserLoginApiView, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
