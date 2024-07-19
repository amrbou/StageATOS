from django.db import models

class Product(models.Model):
    TELEPHONY = 'telephony'
    INTERNET = 'internet'
    PRODUCT_TYPES = [
        (TELEPHONY, 'Telephony'),
        (INTERNET, 'Internet'),
    ]
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default="TELEPHONY")

    def str(self):
        return self.name
    
