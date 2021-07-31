from django.shortcuts import render
from .models import Setting
from Product.models import Product
# Create your views here.
def home(request):
    setting=Setting.objects.get(id=1)
    sliding =Product.objects.all().order_by('id')[:2]

    context={
        'setting':setting,
        'sliding_images':sliding
    }
    return render(request,'EcomApp/home.html', context)