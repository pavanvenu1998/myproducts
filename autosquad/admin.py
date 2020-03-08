from django.contrib import admin
from . models import OrderItem
from . models import Item
from . models import Order
from . models import UserProfile
from . models import Address
from . models import Payment
from . models import Coupon
from . models import Refund

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
