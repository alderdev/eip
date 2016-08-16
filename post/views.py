from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostCreateForm, PostUpdateForm

# Create your views here.
def post_list(request):
    title = "公告列表"
    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    return render(request, "posts_list.html", locals())


def post_create(request):
    title = "新增公告"
    form = PostCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "posts_list.html", locals())

def post_detail(request, id=None):
    title = "公告明細"
    record = get_object_or_404( Post, id=id)
    form = PostUpdateForm(request.POST or None, instance = record)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absoulte_url())

    return render(request, "post_detail.html", locals())

def post_update(request, id=None):
    title = "公告明細"
    record = get_object_or_404( Post, id=id)
    return render(request, "post_list.html", locals())


def post_delete(request, id=None):
    title = "工單列表"
    record = get_object_or_404( Post, id=id)
    return render(request, "post_list.html", locals())
