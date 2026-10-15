from django_filters import rest_framework as filters
from stock import models

class TagsFilterSet(filters.FilterSet):
    model = models.Tags

    class Meta:
        fields = ["id"]

class ProductFilterSet(filters.FilterSet):
    model = models.Product

    class Meta:
        fields = ["id"]