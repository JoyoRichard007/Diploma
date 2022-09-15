from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.models import Etudiant, TraceEtude, DiplomeLMD
from api.serileazers import (
    EtudiantSerileazers,
    TraceEtudeSerileazers,
    DiplomeObtenuSerileazers,
)


class EtudiantViewSet(ModelViewSet):
    serializer_class = EtudiantSerileazers

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]

        return super(EtudiantViewSet, self).get_permissions()

    def get_queryset(self):
        numero_unique = self.request.GET.get("numero")

        if numero_unique and self.request.method == "GET":
            queryset = Etudiant.objects.filter(id=numero_unique)
            if queryset:
                return queryset
            return []

        else:
            return Etudiant.objects.all()


class TraceEtudeViewSet(ModelViewSet):
    serializer_class = TraceEtudeSerileazers

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]

        return super(TraceEtudeViewSet, self).get_permissions()

    def get_queryset(self):
        numero_unique = self.request.GET.get("numero")

        if numero_unique and self.request.method == "GET":
            queryset = TraceEtude.objects.filter(etudiant=numero_unique)
            if queryset:
                return queryset
            return []

        else:
            return TraceEtude.objects.all()


class DiplomeLMDViewSet(ModelViewSet):
    serializer_class = DiplomeObtenuSerileazers

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]

        return super(DiplomeLMDViewSet, self).get_permissions()

    def get_queryset(self):
        numero_unique = self.request.GET.get("numero")

        if numero_unique and self.request.method == "GET":
            queryset = DiplomeLMD.objects.filter(etudiant=numero_unique)
            if queryset:
                return queryset
            return []

        else:
            return DiplomeLMD.objects.all()
