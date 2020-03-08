from rest_framework import serializers
from . models import Item
from . models import Order
from . models import OrderItem
from . models import UserProfile
from . models import Address
from . models import Payment
from . models import Coupon
from . models import Refund


class UserProfileSerializer(serializers.ModelSerializer):

   class Meta:
    model = UserProfile
    fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=Item
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=OrderItem
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields="__all__"

class AddressSerializer(serializers.ModelSerializer):

   class Meta:
    model = Address
    fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):

   class Meta:
    model = Payment
    fields = "__all__"

class CouponSerializer(serializers.ModelSerializer):

   class Meta:
    model =Coupon
    fields = "__all__"

class RefundSerializer(serializers.ModelSerializer):

   class Meta:
    model =Refund
    fields = "__all__"