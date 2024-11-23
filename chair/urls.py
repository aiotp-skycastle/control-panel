from django.urls import path

from . import views

app_name = "chair"
urlpatterns = [
    path("status", views.ChairView.as_view(), name="chair"),
    path("studytime", views.StudyTimeView.as_view(), name="studytime"),
]