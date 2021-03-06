from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
      data = super().validate(attrs)
      refresh = self.get_token(self.user)
      data['access']=str(refresh.access_token)
      data['refresh']=str(refresh)
      data['username']=self.user.username
      data['id']=self.user.id
      return data
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email','username','password','cpf','telephone']
        extra_kwargs = {'password': { 'write_only': True }}
    def create(self, validated_data):
      password = validated_data.pop('password',None)
      cpf = validated_data.pop('cpf',None)
      username = validated_data.pop('username',None)
      email = validated_data.pop('email',None)
      telephone = validated_data.pop('telephone',None)
      instance = self.Meta.model(username=username,email=email,telephone=telephone,cpf=cpf)
      if password is not None:
        instance.set_password(password)
      instance.save()
      return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
