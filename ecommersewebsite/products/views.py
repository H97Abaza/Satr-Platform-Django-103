from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request, "products/home.html")
def products(request):
    products = Product.objects.all()
    paginator=Paginator(products,4)
    page=request.GET.get("page")
    paged_products=paginator.get_page(page)
    context={'products':paged_products}
    return render(request, "products/products.html",context)