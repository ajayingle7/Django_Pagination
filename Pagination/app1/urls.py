from django.urls import path
from .views import productView, showView



urlpatterns = [

    path("product/", productView, name = "product"),
    path("show/", showView, name="show")


]