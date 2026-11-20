from rest_framework import serializers
from .models import Products_details

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products_details
        fields = "__all__"
        
