from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View


class IsUserOrCreatingAccountOrReadOnly(permissions.BasePermission):
    """Object-level permission

    Allows users to create accounts or edit their own accounts.
    """

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        user_is_making_new_account = getattr(view, "action", None) == "create"
        if user_is_making_new_account:
            return True

        is_read_only_action = request.method in permissions.SAFE_METHODS
        if is_read_only_action:
            return True

        is_accessing_their_own_user_object = obj == request.user
        return bool(is_accessing_their_own_user_object)
