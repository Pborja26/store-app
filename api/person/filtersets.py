from django_filters import rest_framework as filters
from person import models

class UserFilterSet(filters.FilterSet):

    class Meta:
        model = models.User
        fields = [
            "id",
            "email",
            "username"
        ]