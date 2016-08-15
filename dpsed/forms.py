from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import WorkOrder

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        #fields = ["category", "zmms", "manage_memo" ]
        exclude = ('create_at','modify' ,'zmms','material_ready_date','estimated_finish',)
        widgets = {
            'customer': forms.TextInput(attrs={'size':20, 'title':'Customer Number', }) ,
            'product': forms.TextInput(attrs={'size':20, 'title':'Product Number', }) ,

        }
