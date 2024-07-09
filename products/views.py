from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product, Category
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy

from products.forms import CategoryForm

# Create your views here.
def product(request):
    products = Product.objects.all()
    name = request.GET.get('name', False)
    cate = request.GET.get('cat', False)

    print(name)
    if name:
        products = products.filter(name__icontains=name)

    if cate:
        products = products.filter(product_category_id=cate)
    
    product_obj = Product.objects.get(id=2)
    categories = Category.objects.all()
    print(products)
    context_name = {
        "product_list":products,
        "object":product_obj,
        "categories":categories,
        "name":"bhuban ghimire",
        "address":"ktm",
        "phone":98629855,
    }
    return render(request,'generic/product_list.html', context=context_name)



def create(request):
    if request.method=='POST':
        print(request.POST)
        pro_name = request.POST.get('name', '')
        price = request.POST.get('price', 1)
        added_by = request.user
        product_category = request.POST.get('product_category', 1)
        cat_obj = Category.objects.get(id=product_category)
        print(type(added_by), type(product_category))
        Product.objects.create(name=pro_name, price=price, added_by=added_by, product_category_id=product_category)
        return redirect(reverse("category_list"))
    else:
        return render(request,'product_list.html')


def category_list(request):
    
    return render(request,'category_list.html')


def category_create(request):
    cat_form = CategoryForm()
    if request.method=="POST":
        data = request.POST
        
        form = CategoryForm(data=data)

        if form.is_valid():
            form.save()
            return redirect(reverse("category_list"))

        else:
            
            return render(request,'category_create.html', {"form":form, "error":form.errors})


    return render(request,'category_create.html', {"form":cat_form})


# list, detail, update, delete, ajax

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, DeleteView

class GenericCategory(ListView):
    model = Category
    template_name = "generic/category_list.html"
    paginate_by = 5

    # def get_queryset(self) -> QuerySet[Any]:
    #     queryset = super().get_queryset()
    #     name = self.request.GET.get("name", False)
    #     if name:
    #         queryset = queryset.filter(name__icontains=name)
    #     return queryset
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cat_list = context['object_list']
        for cat_obj in cat_list:
            cat_obj.product_count = Product.objects.filter(product_category=cat_obj).count()
        context['total_objects'] = Category.objects.all().count()
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = "generic/category_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cat_obj = context['object']
        # for cat_obj in cat_list:
        #     cat_obj.product_count = Product.objects.filter(product_category=cat_obj).count()
        context['total_objects'] = Category.objects.all().count()
        return context
    


class CategoryUpdateView(UpdateView):
    model = Category
    # form_class = CategoryFor
    fields = "__all__"
    template_name = "generic/category_update.html"
    success_url = reverse_lazy('category_list')


# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = "generic/category_detail.html"

    
def category_delete(request, pk):
    id = pk
    try:
        Category.objects.filter(id=id).delete()
        
    except Exception as e:
        print(e)

    return redirect(reverse("category_list"))
    