from django.contrib import admin
from django.urls import path,include
from apps.tasks.urls import urlpatterns as tasks_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',include(tasks_url))
]
