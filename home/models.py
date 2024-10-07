from django.db import models
from django.utils.text import slugify
from decimal import Decimal
from django.utils import timezone

class Product(models.Model):
    # Basic product details
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='products/images/')
    description_image = models.ImageField(upload_to='products/descriptions/')
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount percentage")
    excat_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    discount_cut_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    product_type = models.CharField(max_length=255, help_text="Product type (e.g., storage, color, liters, etc.)")
    product_capacity = models.CharField(max_length=50, help_text="Capacity or specifications (e.g., 512GB, Red, 1L)")
    qrcode_image = models.ImageField(upload_to='products/qrcodes/')
    payment_link = models.CharField(max_length=555)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Ensure discount is handled as Decimal
        if isinstance(self.discount, str):
            self.discount = Decimal(self.discount)

        # Calculate excat_price and discount_cut_price
        self.excat_price = self.actual_price * (1 - (self.discount / Decimal('100')))
        self.discount_cut_price = self.actual_price - self.excat_price
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Address(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    house_no = models.CharField(max_length=100)
    road_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the Product model
    created_at = models.DateTimeField(default=timezone.now)  # Set default to now
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}, {self.city}, {self.state} - {self.product.name}"
