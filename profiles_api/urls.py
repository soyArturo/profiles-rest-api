from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import UserProfileViewSet, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('obtain_token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    # path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
