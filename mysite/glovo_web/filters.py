from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category_name': ['exact'],
            'active': ['exact'],
            'price': ['gt', 'lt'],
        }
