from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from profiles.models import Profile, ProfileStatus
from profiles.api.permissions import IsOwnerProfileOrReadOnly, IsOwnerOrReadOnly
from profiles.api.serializers import (ProfileSerializer, 
                                      ProfileStatusSerializer, 
                                      ProfileAvatarSerializer)

#class to update avatar
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

#example using viewsets generic views, dont ModelViewset
#this way we get the endpoints explicitly
#and use only the ones tha we have
class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]

#example using ModelViewSet
#this way we get all endpoints available
class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

        