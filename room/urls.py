from django.urls import path

from . import views

app_name = "room"
urlpatterns = [
    path("illuminance", views.IlluminanceView.as_view(), name="illuminance"),
    path("temperature", views.TemperatureView.as_view(), name="temperature"),
]