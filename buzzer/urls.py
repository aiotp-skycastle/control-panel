from django.urls import path

from . import views

app_name = "buzzer"
urlpatterns = [
    path("status", views.BuzzerView.as_view(), name="buzzer"),
]