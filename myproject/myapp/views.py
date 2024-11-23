from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Friends
from .serializers import UserSerializer, FriendsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class HelloWorldView(APIView):
    def get(self, request):
        try:
            return Response("hello world", status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GetUserView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
class GetAllUsersView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializers = UserSerializer(users, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:  # Catch generic exceptions if needed
            return Response({"error": "Failed to retrieve users"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UpdateUserView(APIView):
    def put(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
class DeleteUserView(APIView):
    def delete(self, request, username):
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response({"message": "User deleted successfully"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#   
# 
class CreateFriendView(APIView):
    def post(self, request):
        serializer = FriendsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GetAllFriendsView(APIView):
    def get(self, request):
        friends = Friends.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data)
class DeleteFriendView(APIView):
    def delete(self, request, id):
        try:
            friend = Friends.objects.get(id=id)
            friend.delete()
            return Response({"message": "Friend deleted successfully"})
        except Friends.DoesNotExist:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)
class UpdateFriendView(APIView):
    def put(self, request, id):
        try:
            friend = Friends.objects.get(id=id)
            serializer = FriendsSerializer(friend, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Friends.DoesNotExist:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)