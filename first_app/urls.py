from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list", view=views.list_client, name="list_client"),
    path("<int:id>/detail", views.detail, name="detail"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("add-client", views.addClient, name="add"),
    path("contact", views.contact, name="contact"),
    path("products", views.products, name="products"),
    path("<int:id>/update", views.update, name="update"),
    path("test", views.test, name="test"),
]
