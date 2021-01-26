from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import Http404


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'description': obj.description
#     }
#     # context = {'object': obj}
#     return render(request, 'products/product_details.html', context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.object.create(**my_form.cleaned_data) # saves data
#             print(my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#
#     return render(request, 'products/product_create.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)


def render_initial_data(request):
    obj = Product.object.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request, id):
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Product, id=id)
    context = {'object': obj}
    return render(request, 'products/product_details.html', context)


def dynamic_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {'object': obj}
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all()  # list of objects
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
