from django.shortcuts import render

# Create your views here.
def dps_list(request):
    title = "工單列表"
    return render(request, "dpsed_list.html", locals())

def dps_create(request):
    title = "新增工單"
    return render(request, "dpsed_list.html", locals())

def dps_detail(request):
    title = "工單明細"
    return render(request, "dpsed_list.html", locals())


def dps_update(request):
    title = "工單列表"
    return render(request, "dpsed_list.html", locals())


def dps_delete(request):
    title = "工單列表"
    return render(request, "dpsed_list.html", locals())
