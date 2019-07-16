from rest_framework import generics, views
from .models import Profile
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .serializers import RegisterSerializer, ProfileSerializer
from django.http import JsonResponse


# New User Registration
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


# Get Current Profile
class CurrentProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


# Get all Users
class AllUserProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]


# Get Filtered Users
class GenderFilterUserProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        gender = self.kwargs['gen']
        return Profile.objects.filter(gender=gender)


# Get Filtered Users
class CityFilterUserProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        city = self.kwargs['gen']
        return Profile.objects.filter(permanent_add__city=city)


class DetailView(views.APIView):

    def get_object(self, pk):
        return Profile.objects.get(pk=pk)

    def patch(self, request, pk):
        model_object = self.get_object(pk)
        serializer = RegisterSerializer(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")






