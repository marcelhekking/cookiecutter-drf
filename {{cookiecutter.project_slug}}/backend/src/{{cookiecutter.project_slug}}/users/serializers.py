from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: tuple[str, ...] = (
            "id",
            "username",
            "first_name",
            "last_name",
            "url"
        )
        read_only_fields: tuple[str, ...] = ("username",)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict[str, Any]) -> User:
        user: User = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields: tuple[str, ...] =
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "auth_token",
        )
        read_only_fields: tuple[str, ...] = ("auth_token",)
        extra_kwargs: dict[str, dict[str, bool]] = {"password": {"write_only": True}}
