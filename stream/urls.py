from django.urls import path

from . import views

app_name = "stream"
urlpatterns = [
    path('<str:filename>', views.StreamView.as_view(), name='stream'),
    path('', views.StreamUploadView.as_view(), name='stream-upload'),
]