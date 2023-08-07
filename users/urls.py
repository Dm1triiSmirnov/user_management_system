from django.urls import path

from users.views import UserRetrieveDestroyViewSet

urlpatterns = [
    path(
        "<str:username>/",
        UserRetrieveDestroyViewSet.as_view({"get": "retrieve",
                                            "patch": "partial_update",
                                            "delete": "destroy"})
    ),
    ]
