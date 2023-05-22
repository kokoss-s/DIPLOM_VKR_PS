from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('fire/', include('fire.urls')),
    path('admin/', admin.site.urls),
]
