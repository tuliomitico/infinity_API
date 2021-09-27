from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import RegisterUserSerializer, UserSerializer

# Create your views here.
class CustomUserCreate(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        
        # userpk = kwargs.get('pk', 0)
        # user = get_object_or_404(request.user, pk=userpk)
      
        serializeddata = UserSerializer(request.user, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,format=None):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
