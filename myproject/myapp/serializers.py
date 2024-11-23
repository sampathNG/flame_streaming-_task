# from rest_framework import serializers
from .models import User,Friends
from rest_framework_mongoengine.serializers import DocumentSerializer

# class UserSerializer(serializers.ModelSerializer):
# class UserSerializer(DocumentSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gender', 'dateofbirth', 'languages', 'homeTown', 'bio', 'following', 'followers', 'likes', 'created_at']

class UserSerializer(DocumentSerializer):  # Or ModelSerializer
    class Meta:
        model = User  # Ensure this matches your User model
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'gender', 
            'dateofbirth', 'languages', 'homeTown', 'bio', 'following', 
            'followers', 'likes', 'created_at'
        ]

class FriendsSerializer(DocumentSerializer):
    class Meta:
        model = Friends
        fields = ['id', 'fullname', 'active', 'follow', 'user']