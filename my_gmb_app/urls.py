# my_gmb_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/locations/', views.get_locations, name='get_locations'),
    path('api/reviews/<str:location_id>/', views.get_reviews, name='get_reviews'),
]
