from django.urls import path

from users.views import UserRetrieveUpdateDestroyViewSet

urlpatterns = [
    path(
        "profile/<str:username>/",
        UserRetrieveUpdateDestroyViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="user-profile",
    ),
]
