from hanoi_lotto.api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'result/hanoi', views.hannoi_lottoViewSet, basename="vt_result")
router.register(r'result/hanoivip', views.hannoi_vipViewSet, basename="vt_result_vip")
router.register(r'result/hanoispecial', views.hannoi_specialViewSet, basename="vt_result_special")
urlpatterns = router.urls
