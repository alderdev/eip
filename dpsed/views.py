from django.shortcuts import render, get_object_or_404

from .models import WorkOrder

# Create your views here.
#若是一個資料集, 就用queryset
#若是單筆資料, 就用record

def dps_list(request):
    title = "工單列表"
    queryset = WorkOrder.objects.all()

    return render(request, "dpsed_list.html", locals())

def dps_create(request):
    title = "新增工單"
    return render(request, "dpsed_detail.html", locals())

def dps_detail(request, id=None):
    title = "工單明細"
    record = get_object_or_404( WorkOrder, id=id)
    return render(request, "dpsed_detail.html", locals())

def dps_update(request, id=None):
    title = "工單列表"
    record = get_object_or_404( WorkOrder, id=id)
    return render(request, "dpsed_list.html", locals())


def dps_delete(request, id=None):
    title = "工單列表"
    record = get_object_or_404( WorkOrder, id=id)
    return render(request, "dpsed_list.html", locals())
