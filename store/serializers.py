from store.models import Store
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','name','description','slug','logotype','lat','lng','category','owner']
