from django.urls import path
from rest_framework.routers import SimpleRouter
from stock import views

router = SimpleRouter(trailing_slash=True)

router.register(
    r"products",
    views.ProductsViewSet,
    basename="products"
)

router.register(
    r"tags",
    views.TagsViewSet,
    basename="tags"
)

urlpatherns = [
    
]