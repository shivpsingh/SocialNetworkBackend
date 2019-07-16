from django.urls import path
from .views import RegisterAPIView, CurrentProfileAPIView, DetailView
from .views import AllUserProfileAPIView, GenderFilterUserProfileAPIView, CityFilterUserProfileAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register_api_view'),
    path('profile', CurrentProfileAPIView.as_view(), name='my_profile_api_view'),
    path('allprofile', AllUserProfileAPIView.as_view(), name='profile_user_api_view'),
    path('filter/gender/<str:gen>', GenderFilterUserProfileAPIView.as_view(), name='gender_filter_user_api_view'),
    path('filter/address/<str:gen>', CityFilterUserProfileAPIView.as_view(), name='address_filter_user_api_view'),
    # path('update/<int:pk>', DetailView.as_view(), name='update_api_view'),
]
