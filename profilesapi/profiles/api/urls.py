from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileViewSet

# router views created using viewset
# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

#user router to create the routes
router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
    # path("profiles/", profile_list, name="profile-list"),
    # path("profiles/<int:pk>/", profile_detail, name="profile-detail")
]
