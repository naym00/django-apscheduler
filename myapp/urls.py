from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taskapp/', include('taskapp.urls')),
    path('datetaskapp/', include('datetaskapp.urls')),
]
