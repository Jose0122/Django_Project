from django.urls import path,include
from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products",ProductViewSet)

urlpatterns = [
    # path("products/",ProductList.as_view()),
    # path("products/<int:pk>/",ProductDetails.as_view()),
    path("",include(router.urls)),

]