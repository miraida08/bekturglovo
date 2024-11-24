from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(70),
                                                       MinValueValidator(18)], null=True, blank=True)
    ROLE_CHOICES = (
        ('courier', 'courier'),
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES)


class Store(models.Model):
    store_name = models.CharField(max_length=16)
    store_description = models.TextField()
    contact_info = PhoneNumberField(region='KG', null=True, blank=True)
    address = models.CharField(max_length=32, )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                   null=True, blank=True)
    store_image = models.FileField(upload_to='store_image/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.store_name}'

    def get_average_rating(self):
        ratings = self.store_stars.all()
        if ratings.exists():
            return round(sum(rating.store_stars for rating in ratings) / ratings.count(), 1)
        return 0


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    product_name = models.CharField(max_length=16)
    product_description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=1)
    product_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product_store')
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='product_image/', verbose_name='product_images',
                                      null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'


class Order(models.Model):
    client_order = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_order')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_products')
    delivery_address = models.CharField(max_length=32)
    courier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courier_order')
    created_date = models.DateTimeField(auto_now_add=True)
    ORDER_CHOICES = (
        ('ожидает обработки', 'ожидает обработки'),
        ('в процессе доставки', 'в процессе доставки'),
        ('доставлен', 'доставлен'),
        ('отменен', 'отменен')
    )
    status_orders = models.CharField(max_length=24, choices=ORDER_CHOICES, default='ожидает обработки')


class Courier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yser_courier')
    STATUS_COURIER = (
        ('доступен', 'доступен'),
        ('занят', 'занят')
    )
    status_courier = models.CharField(max_length=16, choices=STATUS_COURIER, default='доступен')
    current_orders = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='current_orders')


class Review(models.Model):
    client_review = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_review')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    courier_review = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courier_review')
    rating_review = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)