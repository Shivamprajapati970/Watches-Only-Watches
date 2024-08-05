from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .form import LoginForm


urlpatterns = [
    
    path("",index),
    path("home/",Home),
    path("allproduct/",AllProduct),
    path("category/<int:id>/",CategoryView.as_view(),name="category"),
    path("product_detail/<int:pk>/",ProductDetail.as_view(),name="ProductDetail"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("address/",ProfileView.as_view(),name="address"),
    #path("prodcat_brand/<int:id>/",CategoryBrand.as_view(),name="ProductBrand"),

    # Login Authentication
    path("registration/",CustomerRegistration.as_view(),name="customer_registration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name="login")



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)