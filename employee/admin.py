from django.contrib import admin
from .models import Department, Jobtitle, Person
# Register your models here.



class PersonAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'english_name', 'department', 'jobtitle', 'dutydate' ,)




admin.site.register(Department)
admin.site.register(Jobtitle)
admin.site.register(Person, PersonAdmin)

# Register your models here.
