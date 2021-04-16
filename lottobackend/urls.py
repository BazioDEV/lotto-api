from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('th/', include('gov_lotto.urls')),
    path('laos/', include('lao_lotto.urls')),
    path('hanoi/', include('hanoi_lotto.urls')),
]
