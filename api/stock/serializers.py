from rest_framework import serializers
from stock import models

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"