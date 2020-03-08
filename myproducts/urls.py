"""myproducts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path


from autosquad import views
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path('admin/', admin.site.urls),
     path('UserProfile/', views.UserProfileList.as_view()),
     path('Item/', views.ItemList.as_view()),
     path('OrderItem/', views.OrderItemList.as_view()),
     path('Order/', views.OrderList.as_view()),
     path('Address/', views.AddressList.as_view()),
     path('Payment/', views.PaymentList.as_view()),
     path('Coupon/', views.CouponList.as_view()),
     path('Refund/', views.RefundList.as_view()),

 ]
