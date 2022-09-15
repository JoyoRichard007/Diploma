from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from api.models import Bachelier, DemandeDeDiplome
from rest_framework.permissions import IsAuthenticated
from api.serileazers import DemandeDeDiplomeSerileazers, BachelierSerileazers


class DemandeDeDiplomeViewSet(ModelViewSet):
    serializer_class = DemandeDeDiplomeSerileazers
    permission_classes = (AllowAny,)
    queryset = DemandeDeDiplome.objects.all()


class BachelierViewSet(ModelViewSet):

    serializer_class = BachelierSerileazers

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]

        return super(BachelierViewSet, self).get_permissions()

    def get_queryset(self):
        filtre_num = self.request.GET.get("numero")
        filtre_nom_prenom = self.request.GET.get("nom_prenom")

        if filtre_num and self.request.method == "GET":
            queryset = Bachelier.objects.filter(numero_iscription=filtre_num)
            if queryset:
                return queryset
            return []

        elif filtre_nom_prenom and self.request.method == "GET":
            nom, prenom = filtre_nom_prenom.split("__")
            queryset = Bachelier.objects.filter(
                nom=nom.upper(), prenom=" ".join(prenom.split("_"))
            )
            if queryset:
                return queryset
            return []

        else:
            queryset = Bachelier.objects.all()

        return queryset
