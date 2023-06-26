from django.contrib import admin
from django.urls import path
# from django.conf.urls import include, url

from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordenamiento/', include('ordenamiento.urls')),
    path('', include('ordenamiento.urls')),
]