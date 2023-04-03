from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = "For Sale"
        FOR_RENT = "For Rent"
        
    class HomeType(models.TextChoices):
        HOUSE = "House"
        CONDO = "Condo"
        APARTMENT = "Apartment"
        TOWNHOUSE = "Townhouse"
        
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    sqm = models.DecimalField(decimal_places=2)
    open_house = models.BooleanField(default=False)
    main_photo = models.ImageField(upload_to="/photos/%Y/%m/%d")
    main_1 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    main_2 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    main_3 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    main_4 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    main_5 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    main_6 = models.ImageField(upload_to="/photos/%Y/%m/%d", black=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)
    
    def __str__(self):
        return self.title
    