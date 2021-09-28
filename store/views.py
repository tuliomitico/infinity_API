from store.permissions import StoreOwnerWritePermission
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from .serializers import StoreSerializer
from .models import Store

# Create your views here.
class StoreList(generics.ListCreateAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetail(generics.RetrieveAPIView):

    serializer_class = StoreSerializer

    def get_object(self,queryset = None,**kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Store,slug=item)

class StoreOwnerDetail(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = StoreSerializer
  queryset = Store.objects.all()
class StoreEdit(generics.UpdateAPIView):

    permission_classes = [StoreOwnerWritePermission]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDelete(generics.DestroyAPIView):

  permission_classes = [StoreOwnerWritePermission]
  queryset = Store.objects.all()
  serializer_class = StoreSerializer
