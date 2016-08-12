from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import WorkOrder
from .forms import WorkOrderForm

# Create your views here.
#若是一個資料集, 就用queryset
#若是單筆資料, 就用record

def dps_list(request):
    title = "工單列表"
    queryset_list = WorkOrder.objects.all()

    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    return render(request, "dpsed_list.html", locals())

def dps_create(request):
    title = "新增工單"
    form = WorkOrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "dpsed_form.html", locals())

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
