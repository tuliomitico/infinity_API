import re

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterUserSerializer, UserSerializer, MyTokenObtainPairSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

decorated_login_view = swagger_auto_schema(method='post',responses={status.HTTP_201_CREATED: MyTokenObtainPairSerializer})(MyTokenObtainPairView.as_view())
class CustomUserCreate(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request):
        data = request.data
        rx = re.compile('[-.]')
        data['cpf'] = rx.sub(r'',data['cpf'])
        reg_serializer = RegisterUserSerializer(data=data)
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
