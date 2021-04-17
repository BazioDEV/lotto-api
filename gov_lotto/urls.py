from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from gov_lotto.api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'result', views.gov_thaiViewSet, basename="th_result")

urlpatterns = [
    path('', include(router.urls)),
]