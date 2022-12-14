"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from product_inventory.views import SKUViewSet
from orders.views import OrderViewSet

auth_urls = [
    path('accounts/', include('rest_registration.api.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]  # todo rename

product_inventory_urls = [
    path('', SKUViewSet.as_view({'get': 'list', 'put': 'create'}), name='sku_view_set'),
]

order_urls = [
    path('', OrderViewSet.as_view({'post': 'create'}), name='order viewset'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',  include(auth_urls)),
    path('api/v1/skus/', include(product_inventory_urls)),
    path('api/v1/orders/', include(order_urls)),
]
