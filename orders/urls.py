from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("api/place/", views.api_place_order, name="api-place"),
    path("place/", views.place_order, name="place"),
    path("", views.get_all_orders, name="list")
]