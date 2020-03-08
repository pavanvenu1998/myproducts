from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from . models import Item
from . models import OrderItem
from . models import Order
from . models import UserProfile
from . models import Address
from . models import Payment
from . models import Coupon
from . models import Refund
from . serializers import ItemSerializer
from . serializers import OrderItemSerializer
from . serializers import OrderSerializer
from . serializers import UserProfileSerializer
from . serializers import AddressSerializer
from . serializers import PaymentSerializer
from . serializers import CouponSerializer
from . serializers import RefundSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProfileList(APIView):
    def get(self,request):
        UserProfile1=UserProfile.objects.all()
        serializer=UserProfileSerializer(UserProfile,many=True)
        return Response(serializer.data)


class ItemList(APIView):
    def get(self,request):
        Item1=Item.objects.all()
        serializer=ItemSerializer(Item,many=True)
        return Response(serializer.data)

class OrderItemList(APIView):
    def get(self,request):
        orderItem1=OrderItem.objects.all()
        serializer=OrderItemSerializer(OrderItem,many=True)
        return Response(serializer.data)

class OrderList(APIView):

    def get(self,request):
        Order1=Order.objects.all()
        serializer=OrderSerializer(order,many=True)
        return Response(serializer.data)

class AddressList(APIView):
    def get(self,request):
        Address1=Address.objects.all()
        serializer = AddressSerializer(Address,many=True)
        return Response(serializer.data)


class PaymentList(APIView):
    def get (self,request):
        Payment1=Payment.objects.all()
        serializer=PaymentSerializer(Payment,many=True)
        return Response(serializer.data)


class CouponList(APIView):
    def get(self,request):
        Coupon1=Coupon.objects.all()
        serializer=CouponSerializer(Coupon,many=True)
        return Response(serializer.data)


class RefundList(APIView):
    def get(self,request):
        Refund1=Refund.objects.all()
        serializer=RefundSerializer(Refund,many=True)
        return Response(serializer.data)


    def post(self):
        pass

    def Post(self):
        pass

    def post(self):
        pass

    def post(self):
        pass

    def post(self):
        pass

    def post(self):
        pass

    def post(self):
        pass

    def post(self):
        pass