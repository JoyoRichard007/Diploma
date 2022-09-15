from api.views import *
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL
from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()

router.register("demande", DemandeDeDiplomeViewSet, "demande")
router.register("bacc", BachelierViewSet, "bacc")
router.register("etudiant", EtudiantViewSet, "etudiant")
router.register("traceEtude", TraceEtudeViewSet, "traceEtude")
router.register("diplomeLMD", DiplomeLMDViewSet, "diplomeLMD")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
    path("api/login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
