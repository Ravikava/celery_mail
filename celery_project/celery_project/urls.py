from django.contrib import admin
from django.urls import path

from celery_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello,name="hello"),
]
