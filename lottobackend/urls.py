from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('auth/', obtain_auth_token),
    path('th/', include('gov_lotto.urls')),
    path('laos/', include('lao_lotto.urls')),
    path('hanoi/', include('hanoi_lotto.urls')),
]
