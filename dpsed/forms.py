from django import forms
from .models import WorkOrder

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        #fields = ["category", "zmms", "manage_memo" ]
        exclude = ('create_at','modify' ,)
