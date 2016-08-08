from django.contrib import admin

from .models import WorkOrder, Product, CycleStatus,Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'title','contect','phone','phone_ext', 'email', 'address' ,)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'product_desc', 'specification' ,'cycle_status',)

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ( 'recevice_date', 'ships_order','work_order','product',  'ord_amount', 'deliverly' ,)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CycleStatus)
