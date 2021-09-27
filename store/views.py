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

class StoreEdit(generics.UpdateAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDelete(generics.DestroyAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer