from django.shortcuts import render

# Create your views here.
# my_gmb_app/views.py
from django.http import JsonResponse
from .gmb_client import get_gmb_service

def get_locations(request):
    # Fetch a list of locations for the authenticated user
    service = get_gmb_service()
    locations = service.accounts().locations().list(parent='accounts/*').execute()
    return JsonResponse(locations)

def get_reviews(request, location_id):
    # Fetch reviews for a specific location
    service = get_gmb_service()
    reviews = service.accounts().locations().reviews().list(
        name=f'accounts/*/locations/{location_id}',
        pageSize=10
    ).execute()
    return JsonResponse(reviews)
