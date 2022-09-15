from api.models import *
from rest_framework import generics
from api.serileazers import RegisterSerializer


from api.permissions import IsAdminAuthenticated


class RegisterView(generics.CreateAPIView):

    queryset = UserAdmin.objects.all()
    permission_classes = (IsAdminAuthenticated,)
    serializer_class = RegisterSerializer
