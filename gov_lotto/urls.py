from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gov_lotto.api import views

router = DefaultRouter()
router.register(r'result', views.gov_thaiViewSet, basename="th_result")

urlpatterns = [
    path('', include(router.urls)),
]
