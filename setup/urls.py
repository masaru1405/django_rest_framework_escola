from django.contrib import admin
from django.urls import path, include

from escola.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
