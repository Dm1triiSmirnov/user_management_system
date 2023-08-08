from django.urls import path

from users.views import UserRetrieveUpdateDestroyViewSet

urlpatterns = [
    path(
        "<str:username>/",
        UserRetrieveUpdateDestroyViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
]
