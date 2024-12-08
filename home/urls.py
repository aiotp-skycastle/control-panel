from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('desk1/', views.desk1_view, name='desk1'),
    path("", views.HomeView.as_view(), name="home"),
]