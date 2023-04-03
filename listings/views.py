from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models  import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timezone, timedelta

class ListingsView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Listing.objects.order_by("-list_date").filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = "slug"
    
class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by("-list_date").filter(is_published=True)
    serializer_class = ListingDetailSerializer
    lookup_field = "slug"
    
class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer
    
    def post(self,request,format=None):
        queryset = Listing.objects.order_by("-list_date").filter(is_published=True)
        data = self.request.data
        
        sale_type = data["sale-type"]
        queryset = queryset.filter(sale_type__iexact=sale_type)
        
        price = data["price"]
        if price == "$0+":
            price = 0
        elif price == "$200,000+":
            price = 200000
        elif price == "$400,000+":
            price = 400000
        elif price == "$600,000+":
            price = 600000
        elif price == "$800,000+":
            price = 800000
        elif price == "$1,000,000+":
            price = 1000000
        elif price == "$1,200,000+":
            price = 1200000
        elif price == "$1,500,000+":
            price = 1500000
        elif price == "Any":
            price = -1
            
        if price != -1:
           queryset = queryset.filter(price__gte=price)
        
        bedrooms = data["bedrooms"]
        if bedrooms == "0+":
            bedrooms = 0
        elif bedrooms == "1+":
            bedrooms = 1
        elif bedrooms == "2+":
            bedrooms = 2
        elif bedrooms == "3+":
            bedrooms = 3
        elif bedrooms == "4+":
            bedrooms = 4
        elif bedrooms == "5+":
            bedrooms = 5
        
        queryset = queryset.filter(bedrooms__gte=bedrooms)
        
        home_type = data["home_type"]
        queryset = queryset.filter(home_type_iexact=home_type)
        
        bathrooms = data["bathrooms"]
        if bathrooms == "0+":
            bathrooms = 0.0
        elif bathrooms == "1+":
            bathrooms = 1.0
        elif bathrooms == "2+":
            bathrooms = 2.0
        elif bathrooms == "3+":
            bathrooms = 3.0
        elif bathrooms == "4+":
            bathrooms = 4.0
        elif bathrooms == "5+":
            bathrooms = 5.0
        
        queryset = queryset.filter(bathrooms__gte=bathrooms)
        
        sqm = data["sqm"]
        if sqm == "90+":
            sqm = 90.00
        elif sqm == "150+":
            sqm = 150.00
        elif sqm == "200+":
            sqm = 200.00
        elif sqm == "300+":
            sqm = 300.00
        elif sqm == "400+":
            sqm = 400.00
        elif sqm == "500+":
            sqm = 500.00
        
        queryset = queryset.filter(sqm__gte=sqm)
        
        has_photos = data["has_photos"]
        if has_photos == "1+":
            has_photos = 1
        elif has_photos == "2+":
            has_photos = 2
        elif has_photos == "3+":
            has_photos = 3
        elif has_photos == "4+":
            has_photos = 4
        elif has_photos == "5+":
            has_photos = 5
        
        
        for query in queryset:
            count = 0
            if query.main_1:
                count += 1
            if query.main_2:
                count += 1
            if query.main_3:
                count += 1
            if query.main_4:
                count += 1
            if query.main_5:
                count += 1
            if query.main_6:
                count += 1
            
            if count < has_photos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)
        
        open_house = data["open_house"]
        queryset = queryset.filter(open_house__iexact=open_house)
        
        keywords = data["keywords"]
        queryset = queryset.filter(description__icontains=keywords)
        
        serializer = ListSerializer(queryset,many=True)
        return Response(serializer.data)
        
