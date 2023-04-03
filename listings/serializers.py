from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ("slug","title",
                  "address","city",
                  "state","zipcode",
                  "description","sale_type",
                  "price","bedrooms","bathrooms",
                  "home_type","sqm","open_house",
                  "main_photo")
        
class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
        lookup_field = "slug"