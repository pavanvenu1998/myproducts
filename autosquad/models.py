
from django.db import models
from django.conf import settings


ADDRESS_CHOICES=(
    ('B','Billing'),
    ('S','Shipping'),
)

class UserProfile(models.Model):
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_customer_id =models.CharField(max_length=50,blank=True,null=True)
    one_click_purchasing=models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Item(models.Model):
    title=models.CharField(max_length=20)
    price=models.FloatField()


    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    discount_price = models.FloatField(blank=True, null=True)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return str(self.quantity)

    def get_total_item_price(self):
        return self.quantity * self.get_total_item_price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey(
        'Address',related_name='shipping_address', on_delete=models.SET_NULL,blank=True,null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL,blank=True,null=True)
    payment=models.ForeignKey(
        'payment',on_delete=models.SET_NULL, blank=True,null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    '''
    1.Adding a billing address(Failed checkout)
    2.payment
    (Preprocessing , processing , packaging etc.)
    3.Being delivered
    4.Received
    5.Refunds
    '''

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

class Address(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address =models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    address_type = models.CharField(max_length=1,choices=ADDRESS_CHOICES)
    flatno = models.IntegerField(default=False)
    default = models.BooleanField(default=False)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural ='Address'

class Payment(models.Model):
    stripe_charge_id= models.CharField(max_length=40)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True,null=True)
    amount=models.FloatField()
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Coupon(models.Model):
    code=models.CharField(max_length=20)
    amount=models.FloatField()

    def __str__(self):
        return self.code

class Refund(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    reason=models.TextField()
    accepted = models.BooleanField(default=False)
    email=models.EmailField()


    def __str__(self):
        return f"{self.pk}"
