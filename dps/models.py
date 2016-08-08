from django.db import models


class CycleStatus(models.Model):
    description = models.CharField(max_length=36, null=False, blank=False)
    invalid = models.BooleanField(default=True)

    def __str__(self):
        return self.description



# Create your models here.
class Customer(models.Model):
    sap_no = models.CharField(max_length=36, null=True, blank=True)
    title = models.CharField(max_length=36, null=False, blank=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    contect = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    phone_ext  = models.CharField(max_length=100, null=True, blank=True)
    faxno = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    invalid = models.BooleanField(default=True)


    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.title ) )


class Product(models.Model):
    sap_no = models.CharField(max_length=36, null=False, blank=False)
    product_desc = models.CharField(max_length=36, null=False, blank=False)
    specification = models.CharField(max_length=100, null=False, blank=False)
    cycle_status = models.ForeignKey(CycleStatus)
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def __str__(self):
        return ("%s : %s" % (self.sap_no,self.product_desc ) )




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



class WorkOrder(models.Model):
    zmms = models.CharField(max_length=30, blank=True, null=True)
    recevice_date = models.DateField(auto_now =True) #  收單日
    material_ctrl = models.CharField(max_length=30, blank=True, null=True) #物料控管
    workday = models.IntegerField(default= 1) #工作天
    ships_order = models.CharField(max_length=16, null=False, blank=False) # SAP訂單號碼
    customer = models.ForeignKey(Customer) #客戶編號
    work_order = models.CharField(max_length=16, null=False, blank=False) # SAP工單號碼
    product = models.ForeignKey(Product) #  SAP料號
    ord_amount = models.IntegerField(default=1, blank=False, null=False) # 數量
    deliverly = models.DateField(blank=True, null=True) #  業務交期
    material_ready_date = models.DateField(blank=True, null=True) #  齊料日
    estimated_finish = models.DateField(blank=True, null=True) # 預計完工日
    reuqest_user = models.CharField(max_length=16, null=False, blank=False) # 申請人
    material_duty = models.CharField(max_length=16, null=False, blank=False) # 備料人
    comfirm = models.CharField(max_length=30,blank=True, null=True) # 確認
    manage_memo = models.TextField(blank=True, null=True) # 生管備註

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)
