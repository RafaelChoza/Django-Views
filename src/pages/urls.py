from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("saludo/", views.saludo, name="saludo"),
    path("productos/", views.productos, name="productos")
]
