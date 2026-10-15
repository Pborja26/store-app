from utils.views import BaseModelViewSet
from stock import models as stock_models
from stock import serializers as stock_serializers
from stock import filtersets as stock_filters
# Create your views here.

class ProductsViewSet(BaseModelViewSet):
    queryset = stock_models.Product.objects.all()
    filterset_class = stock_filters.ProductFilterSet
    serializer_class = stock_serializers.ProductSerializer

class TagsViewSet(BaseModelViewSet):
    queryset = stock_models.Tags.objects.all()
    filterset_class = stock_filters.TagsFilterSet
    serializer_class = stock_serializers.TagsSerializer
