from .models import Listing
from rest_framework import serializers

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
    
