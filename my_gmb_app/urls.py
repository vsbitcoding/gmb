from django.urls import path
from my_gmb_app import views

urlpatterns = [
    # URLs for GMB APIs
    path('list_locations/', views.ListLocationsView.as_view(), name='list_locations'),
    path('location_reviews/<str:location_id>/', views.LocationReviewsView.as_view(), name='location_reviews'),
    path('update_location/<str:location_id>/', views.UpdateLocationView.as_view(), name='update_location'),
    path('create_location/', views.CreateLocationView.as_view(), name='create_location'),
    path('location_photos/<str:location_id>/', views.LocationPhotosView.as_view(), name='location_photos'),
    path('delete_location/<str:location_id>/', views.DeleteLocationView.as_view(), name='delete_location'),
    path('respond_to_review/<str:location_id>/<str:review_id>/', views.RespondToReviewView.as_view(), name='respond_to_review'),
    path('location_insights/<str:location_id>/', views.LocationInsightsView.as_view(), name='location_insights'),
    path('location_attributes/<str:location_id>/', views.LocationAttributesView.as_view(), name='location_attributes'),
    path('location_categories/<str:location_id>/', views.LocationCategoriesView.as_view(), name='location_categories'),
    path('location_questions/<str:location_id>/', views.LocationQuestionsView.as_view(), name='location_questions'),
    path('answer_question/<str:location_id>/<str:question_id>/', views.AnswerQuestionView.as_view(), name='answer_question'),
    path('location_search/<str:location_id>/', views.LocationSearchView.as_view(), name='location_search'),
    path('location_posts/<str:location_id>/', views.LocationPostsView.as_view(), name='location_posts'),
    path('create_location_post/<str:location_id>/', views.CreateLocationPostView.as_view(), name='create_location_post'),
    path('location_insights_time_series/<str:location_id>/', views.LocationInsightsTimeSeriesView.as_view(), name='location_insights_time_series'),
    path('location_media/<str:location_id>/', views.LocationMediaView.as_view(), name='location_media'),
    path('location_google_updates/<str:location_id>/', views.LocationGoogleUpdatesView.as_view(), name='location_google_updates'),
    path('create_location_question/<str:location_id>/', views.CreateLocationQuestionView.as_view(), name='create_location_question'),
    path('delete_location_question/<str:location_id>/<str:question_id>/', views.DeleteLocationQuestionView.as_view(), name='delete_location_question'),
    path('get_location/<str:location_id>/', views.GetLocationView.as_view(), name='get_location'),
    path('location_attributes_metadata/', views.LocationAttributesMetadataView.as_view(), name='location_attributes_metadata'),
    path('location_review_replies/<str:location_id>/<str:review_id>/', views.LocationReviewRepliesView.as_view(), name='location_review_replies'),
    path('create_review_reply/<str:location_id>/<str:review_id>/', views.CreateReviewReplyView.as_view(), name='create_review_reply'),
    path('location_users/<str:location_id>/', views.LocationUsersView.as_view(), name='location_users'),
]
