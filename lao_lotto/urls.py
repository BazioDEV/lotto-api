from rest_framework.routers import DefaultRouter

from lao_lotto.api import views

router = DefaultRouter()
router.register(r'result', views.lao_lottoViewSet, basename="lao_result")
router.register(r'vip-result', views.lao_vipViewSet, basename="lao_result_vip")
urlpatterns = router.urls
