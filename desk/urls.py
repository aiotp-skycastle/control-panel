from django.urls import path

from . import views

app_name = "desk"
urlpatterns = [
    path("call", views.CallView.as_view(), name="call"),
    path("servo", views.ServoView.as_view(), name="servo"),
]