from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import WorkOrder
from .models import Customer
from .forms import WorkOrderCreateForm, WorkOrderUpdateForm

# Create your views here.
#若是一個資料集, 就用queryset
#若是單筆資料, 就用record

def customer_name(request,id):

    obj = get_object_or_404( Customer, sap_no=id)
    print(obj.title)
    return render(request, "customer.html", locals())



def dps_list(request):
    title = "工單列表"
    queryset_list = WorkOrder.objects.all()

    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, "dpsed_list.html", locals())

def dps_create(request):
    title = "新增工單"
    form = WorkOrderCreateForm(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        print("Successfully is_valid")
        instance = form.save(commit=False)
        instance.save()

        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absoulte_url())
    #else:
        #messages.error(request, "Has Error ")

    return render(request, "dpsed_form.html", locals())

def dps_detail(request, id=None):
    title = "工單明細"
    record = get_object_or_404( WorkOrder, id=id)

    print(record.customer.title)


    form = WorkOrderUpdateForm(request.POST or None, instance = record)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully by Save")
        return HttpResponseRedirect(instance.get_absoulte_url())


    return render(request, "dpsed_form.html", locals())

def dps_update(request, id=None):
    title = "工單列表"
    record = get_object_or_404( WorkOrder, id=id)
    return render(request, "dpsed_list.html", locals())


def dps_delete(request, id=None):
    title = "工單列表"
    record = get_object_or_404( WorkOrder, id=id)
    return render(request, "dpsed_list.html", locals())
