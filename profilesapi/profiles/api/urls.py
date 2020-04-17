from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import (ProfileViewSet, 
                                ProfileStatusViewSet, 
                                AvatarUpdateView)

#user router to create the routes
#it generate all endpoints available in the view class 
router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("avatar", AvatarUpdateView.as_view(), name="avatar-update")
    # path("profiles/", profile_list, name="profile-list"),
    # path("profiles/<int:pk>/", profile_detail, name="profile-detail")
]
