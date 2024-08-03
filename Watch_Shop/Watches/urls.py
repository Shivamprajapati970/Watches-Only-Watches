from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path("",index),
    path("home/",Home),
    path("allproduct/",AllProduct),
    path("category/<int:id>/",CategoryView.as_view(),name="category"),
    path("product_detail/<int:pk>/",ProductDetail.as_view(),name="ProductDetail"),
    #path("prodcat_brand/<int:id>/",CategoryBrand.as_view(),name="ProductBrand"),

    path("registration/",CustomerRegistration.as_view(),name="customer_registration")


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)