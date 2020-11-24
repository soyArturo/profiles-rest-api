from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated



from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from .serializers import UserProfileSerializer, ProfileFeedItemSerializer


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


# class UserLoginApiView(ObtainAuthToken):
#     """Handle creating user auth tokens"""
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
