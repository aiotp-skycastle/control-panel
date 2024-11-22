"""
URL configuration for control_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stream import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buzzer/', include('buzzer.urls')),
    path('chair/', include('chair.urls')),
    path('desk/', include('desk.urls')),
    path('room/', include('room.urls')),
    path('studytime/', include('studytime.urls')),
    path('', include('home.urls')),
    path('stream/<str:filename>', views.StreamView.as_view(), name='stream'),
    path('stream/', views.StreamUploadView.as_view(), name='stream-upload'),

    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
