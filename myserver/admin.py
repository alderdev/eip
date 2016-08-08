from django.contrib import admin
from .models import Status ,Server, Service, Pattern
# Register your models here.

class ServiceInline(admin.TabularInline):
    model = Service


class ServerAdmin(admin.ModelAdmin):
    list_display = ( 'host_name', 'describe', 'intranet_ip' ,)
    inlines = [ServiceInline,]


admin.site.register(Service)
admin.site.register(Status)
admin.site.register(Pattern)
admin.site.register(Server, ServerAdmin)
