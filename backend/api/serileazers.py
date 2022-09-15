from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=UserAdmin.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserAdmin
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password2",
            "province",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = UserAdmin.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            province=validated_data["province"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # Add extra responses here
        data["username"] = self.user.username
        data["id"] = self.user.id
        data["province"] = self.user.province
        data["super"] = self.user.is_superuser

        return data


class DemandeDeDiplomeSerileazers(ModelSerializer):
    class Meta:
        model = DemandeDeDiplome
        fields = "__all__"


class BachelierSerileazers(ModelSerializer):
    class Meta:
        model = Bachelier
        fields = "__all__"


class EtudiantSerileazers(ModelSerializer):
    class Meta:
        model = Etudiant
        fields = "__all__"


class TraceEtudeSerileazers(ModelSerializer):
    class Meta:
        model = TraceEtude
        fields = "__all__"


class DiplomeObtenuSerileazers(ModelSerializer):
    class Meta:
        model = DiplomeLMD
        fields = "__all__"
