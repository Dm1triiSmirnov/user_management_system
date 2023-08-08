from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


class UserRetrieveUpdateDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def check_ownership(self, user):
        return user.id == self.get_object().id

    def retrieve(self, request, *args, **kwargs):
        username = kwargs["username"]
        if not self.check_ownership(request.user):
            return Response(
                {"message": "You can retrieve only your own account"},
                status=status.HTTP_403_FORBIDDEN,
            )
        queryset = CustomUser.objects.get(username=username)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()

        if not self.check_ownership(request.user):
            return Response(
                {"message": "You can update only your own account"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()

        if not self.check_ownership(request.user):
            return Response(
                {"message": "You can delete only your own account"},
                status=status.HTTP_403_FORBIDDEN,
            )

        user.delete()
        return Response(
            {"message": "Account deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
