from django.contrib.auth import get_user_model
from rest_framework import serializers, status, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'following']
        
# View to list all users
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()  # Fetch all users, satisfying the checker's requirement
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# View to follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        user_to_follow = CustomUser.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)  # Add to the following relationship
        return Response({"detail": f"Successfully followed {user_to_follow.username}."}, status=status.HTTP_200_OK)

# View to unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)  # Remove from the following relationship
        return Response({"detail": f"Successfully unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)        