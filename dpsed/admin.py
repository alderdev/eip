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
    list_display = ( 'category','work_order', 'zmms', 'material_ctrl', 'recevice_date', 'ships_order','customer','reuqest_user','material_duty','product',  'ord_amount', 'deliverly' ,'manage_memo')
    list_display_links = ('work_order',)
    list_filter = ('category', 'zmms','material_ctrl','material_duty',)
    search_fields = ['work_order','reuqest_user']
    list_per_page = 10




admin.site.register(OrderCategory)
admin.site.register(CycleStatus)
admin.site.register(ZmmsOption)
admin.site.register(MaterialCtrlOption)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(QuoteHead, QuoteAdmin)
