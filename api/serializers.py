from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', )


class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'phone_number', 'gender', 'dob', )

    def create(self, validated_data):

        user = User()
        user.username = validated_data['user']['username']
        user.email = validated_data['user']['email']
        user.password = validated_data['user']['password']
        user.save()

        profile_data = dict()
        profile_data['user'] = user
        profile_data['phone_number'] = validated_data['phone_number']
        profile_data['gender'] = validated_data['gender']
        profile_data['dob'] = validated_data['dob']
        profile = Profile.objects.create(**profile_data)

        return profile


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    permanent_add = AddressSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'gender', 'profile_pic', 'permanent_add', 'friends')
