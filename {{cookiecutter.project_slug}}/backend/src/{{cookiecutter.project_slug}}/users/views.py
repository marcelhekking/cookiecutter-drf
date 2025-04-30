from typing import List, Type

from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.serializers import Serializer

from .models import User
from .permissions import IsUserOrCreatingAccountOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


@extend_schema(tags=["users"])
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Users viewset

    This viewset handles user-related operations:
    1. Creates a new user
    2. Retrieves user details (requires authentication)
    3. Updates user information (only for the person requesting the update)
    4. Lists all users (requires authentication)
    """

    queryset = User.objects.all()
    serializer_class: Type[Serializer] = UserSerializer
    permission_classes: List[Type[BasePermission]] = [IsUserOrCreatingAccountOrReadOnly]
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self) -> List[BasePermission]:
        if self.action in ["list", "retrieve"]:
            # Require authentication for listing users
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self) -> Type[Serializer]:
        """Returns the appropriate serializer class based on the action."""
        is_creating_a_new_user = self.action == "create"
        if is_creating_a_new_user:
            return CreateUserSerializer
        return self.serializer_class
