from django.urls import path

from . import views

app_name = "chair"
urlpatterns = [
    path("", views.ChairView.as_view(), name="chair"),
]