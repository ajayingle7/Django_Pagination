from django.shortcuts import render
from .models import Product
from django.core.paginator import  Paginator
from .forms import ProductForm
# Create your views here.



def productView(request):
    template_name = "app1/product.html"
    form = ProductForm()
    context = {"form":form}

    if request.method=="POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()


    return render(request,template_name,context)



def showView(request):
    template_name = "app1/show.html"
    post = Product.objects.all()
    p= Paginator(post,2)

    page_number =  request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)

    except PageNotAnInteger:
        page_obj = p.page(1)

    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {"page_obj":page_obj}


    return render(request,template_name,context)
