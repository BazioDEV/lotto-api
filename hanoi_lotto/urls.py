from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'result/hanoi', views.hannoi_lottoViewSet, basename="vt_result")
router.register(r'result/honoivip', views.hannoi_vipViewSet, basename="vt_result_vip")
router.register(r'result/hanoispecial', views.hannoi_specialViewSet, basename="vt_result_special")
urlpatterns = router.urls


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]