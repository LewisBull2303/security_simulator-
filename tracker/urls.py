from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("submit", views.submit_login, name="submit_login"),
    path("training", views.training_page, name="training"),
]
