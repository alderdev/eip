from django.db import models

# Create your models here.


class QuoteHead(models.Model):
    request_user = models.CharField(max_length=60, null=False, blank=False) #開單人
    ord_date = models.DateField() #報價日期
    customer = models.ForeignKey(Customer) #客戶編號
    effective_date = models.DateField() # 報價單有效日期
    invalid = models.BooleanField(default=False) #作廢
    memo = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)



class QuoteDetail(models.Model):
    quotehead = models.ForeignKey(QuoteHead) #報價單編號
    line_no = models.IntegerField() #行號
    product = models.ForeignKey(Product) # 料號
    unit_price = models.FloatField() # 單價
    line_memo = models.CharField(max_length=50, blank=True, null=True) # 行備註
    invalid = models.BooleanField(default=False) #作廢

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)



class SaleOrder(models.Model):
    request_user = models.CharField(max_length=60, null=False, blank=False)
    ord_date = models.DateField()
    customer_title = models.CharField(max_length=60, null=False, blank=False)
    ships_order = models.CharField(max_length=16, null=False, blank=False)
    product = models.ForeignKey(Product)
    ord_amount = models.IntegerField(default=1, blank=False, null=False)
    delivery = models.DateField()
    memo = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)
