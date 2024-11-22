from django.urls import path

from . import views

app_name = "stream_desk"
urlpatterns = [
    path('<str:filename>', views.StreamDeskView.as_view(), name='stream-desk'),
    path('', views.StreamDeskUploadView.as_view(), name='stream-desk-upload'),
]