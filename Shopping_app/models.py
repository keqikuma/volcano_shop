from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CONDITION_CHOICES = [
        ('new', '全新'),
        ('90', '九成新'),
        ('80', '八成新'),
        ('other', '其他'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='other')
    tags = models.CharField(max_length=100, blank=True)  # 或后续改 ManyToManyField
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.condition}) - {self.price}元"
