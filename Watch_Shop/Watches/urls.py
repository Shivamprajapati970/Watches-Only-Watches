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
    path("address/",address,name="address"),
    path("updateAddress/<int:pk>/",UpdateAddress.as_view(),name="updateAddress"),
    path("deletaddress/<int:pk>/",deletaddress,name="deletaddress"),
    path("add_to_cart/",add_to_cart,name="add_to_cart"),
    path("cart/",show_cart,name="showcart"),
    path("checkout",checkout.as_view(),name='checkout'),
    path("remove_item/<int:id>/",remove_item, name="remove_item"),
    path("increase_quantity/<int:pk>/",increase_quantity,name="increase_quantity"),
    path("decrease_quantity/<int:pk>/",decrease_quantity,name="decrease_quantity"),
    path('paymentdone/',payment_done,name="paymentdone"),
    path("orders/",Home,name="orders"),

    #path("prodcat_brand/<int:id>/",CategoryBrand.as_view(),name="ProductBrand"),

    # Login Authentication
    path("registration/",CustomerRegistration.as_view(),name="customer_registration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name="login"),
    path("logout/",auth_view.LogoutView.as_view(next_page='login'),name="logout")



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)