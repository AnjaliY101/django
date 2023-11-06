from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("whaleshark", views.a, name="whaleshark"),
    path("login", views.login_form, name="login"),
    path("login_submit", views.handle_login, name="login_submit"),
]

