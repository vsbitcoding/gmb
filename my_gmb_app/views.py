# my_gmb_app/views.py
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from .gmb_client import get_gmb_service
from rest_framework.response import Response
from rest_framework import status

class ListLocationsView(APIView):
    def get(self, request, *args, **kwargs):
        service = get_gmb_service()
        locations = service.accounts().locations().list(parent='accounts/*').execute()
        return JsonResponse(locations)
    
class LocationReviewsView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        reviews = service.accounts().locations().reviews().list(name=f'accounts/*/locations/{location_id}', pageSize=10).execute()
        return JsonResponse(reviews)

class UpdateLocationView(APIView):
    def patch(self, request, location_id, *args, **kwargs):
        try:
            service = get_gmb_service()
            
            # Retrieve the existing location data from the GMB API
            existing_location = service.accounts().locations().get(name=f'accounts/*/locations/{location_id}').execute()

            # Get the updated location data from the request data
            updated_location_data = request.data

            # Merge the existing data with the updated data
            new_location_data = {**existing_location, **updated_location_data}

            # Perform the update by sending a PATCH request to the GMB API
            response = service.accounts().locations().patch(name=f'accounts/*/locations/{location_id}', body=new_location_data).execute()

            return JsonResponse(response)

        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
        
class CreateLocationView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            service = get_gmb_service()

            # Get the new location data from the request data
            new_location_data = request.data

            # Perform the creation by sending a POST request to the GMB API
            response = service.accounts().locations().create(parent='accounts/*', body=new_location_data).execute()

            return JsonResponse(response)

        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

class LocationPhotosView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        photos = service.accounts().locations().listPhotos(parent=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(photos)

class DeleteLocationView(APIView):
    def delete(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        response = service.accounts().locations().delete(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(response)

class RespondToReviewView(APIView):
    def post(self, request, location_id, review_id, *args, **kwargs):
        service = get_gmb_service()
        reply_text = {
            'comment': 'Thank you for your review!'
        }
        response = service.accounts().locations().reviews().reply(
            name=f'accounts/*/locations/{location_id}/reviews/{review_id}',
            body=reply_text
        ).execute()
        return JsonResponse(response)

class LocationInsightsView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        insights = service.accounts().locations().reportInsights(name=f'accounts/*/locations/{location_id}', body={}).execute()
        return JsonResponse(insights)

class LocationAttributesView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        attributes = service.accounts().locations().getAttributes(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(attributes)

class LocationCategoriesView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        categories = service.accounts().locations().listCategories(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(categories)

class LocationQuestionsView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        questions = service.accounts().locations().listQuestions(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(questions)

class AnswerQuestionView(APIView):
    def post(self, request, location_id, question_id, *args, **kwargs):
        service = get_gmb_service()
        answer_data = {
            'text': 'Your answer here'
        }
        response = service.accounts().locations().questions().answers().create(
            name=f'accounts/*/locations/{location_id}/questions/{question_id}', body=answer_data
        ).execute()
        return JsonResponse(response)

class LocationSearchView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        search_data = {
            'locationName': 'Your Location Name',
            'address': {
                'addressLines': ['123 Main St'],
                'locality': 'Anytown',
                'administrativeArea': 'CA',
                'postalCode': '12345',
                'country': 'US'
            }
        }
        results = service.accounts().locations().search(name=f'accounts/*/locations/{location_id}', body=search_data).execute()
        return JsonResponse(results)

class LocationPostsView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        posts = service.accounts().locations().localPosts().list(name=f'accounts/*/locations/{location_id}', pageSize=10).execute()
        return JsonResponse(posts)

class CreateLocationPostView(APIView):
    def post(self, request, location_id, *args, **kwargs):
        try:
            service = get_gmb_service()

            # Get the new post data from the request data
            new_post_data = request.data

            # Perform the creation by sending a POST request to the GMB API
            response = service.accounts().locations().localPosts().create(
                parent=f'accounts/*/locations/{location_id}',
                body=new_post_data
            ).execute()

            return JsonResponse(response)

        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

class LocationInsightsTimeSeriesView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        time_series_data = service.accounts().locations().reportInsightsTimeSeries(name=f'accounts/*/locations/{location_id}', body={}).execute()
        return JsonResponse(time_series_data)

class LocationMediaView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        media_data = service.accounts().locations().media().list(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(media_data)

class LocationGoogleUpdatesView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        updates = service.accounts().locations().localPosts().list(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(updates)

class CreateLocationQuestionView(APIView):
    def post(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        question_data = {
            'text': 'Your question here'
        }
        response = service.accounts().locations().questions().create(name=f'accounts/*/locations/{location_id}', body=question_data).execute()
        return JsonResponse(response)

class DeleteLocationQuestionView(APIView):
    def delete(self, request, location_id, question_id, *args, **kwargs):
        service = get_gmb_service()
        response = service.accounts().locations().questions().delete(name=f'accounts/*/locations/{location_id}/questions/{question_id}').execute()
        return JsonResponse(response)

class GetLocationView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        location = service.accounts().locations().get(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(location)

class LocationAttributesMetadataView(APIView):
    def get(self, request, *args, **kwargs):
        service = get_gmb_service()
        attributes_metadata = service.attributes().list().execute()
        return JsonResponse(attributes_metadata)

class LocationReviewRepliesView(APIView):
    def get(self, request, location_id, review_id, *args, **kwargs):
        service = get_gmb_service()
        replies = service.accounts().locations().reviews().replies().list(parent=f'accounts/*/locations/{location_id}/reviews/{review_id}').execute()
        return JsonResponse(replies)

class CreateReviewReplyView(APIView):
    def post(self, request, location_id, review_id, *args, **kwargs):
        service = get_gmb_service()
        reply_text = {
            'comment': 'Your reply to the review here'
        }
        response = service.accounts().locations().reviews().replies().create(parent=f'accounts/*/locations/{location_id}/reviews/{review_id}', body=reply_text).execute()
        return JsonResponse(response)

class LocationUsersView(APIView):
    def get(self, request, location_id, *args, **kwargs):
        service = get_gmb_service()
        users = service.accounts().locations().getUsers(name=f'accounts/*/locations/{location_id}').execute()
        return JsonResponse(users)
