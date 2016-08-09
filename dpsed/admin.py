from django.contrib import admin

from .models import WorkOrder, Product, CycleStatus,Customer, QuoteHead, QuoteDetail,ZmmsOption, MaterialCtrlOption, OrderCategory

# Register your models here.
class QuoteDetailInline(admin.TabularInline):
    model = QuoteDetail

class QuoteAdmin(admin.ModelAdmin):
    inlines = [QuoteDetailInline,]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'title','contect','phone','phone_ext', 'email', 'address' ,)

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'sap_no', 'product_desc', 'specification' ,'cycle_status',)

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ( 'category','work_order', 'zmms', 'material_ctrl', 'recevice_date', 'ships_order','customer','reuqest_user','product',  'ord_amount', 'deliverly' ,'manage_memo')




admin.site.register(OrderCategory)
admin.site.register(CycleStatus)
admin.site.register(ZmmsOption)
admin.site.register(MaterialCtrlOption)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(QuoteHead, QuoteAdmin)
