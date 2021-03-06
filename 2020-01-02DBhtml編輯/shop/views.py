from django.shortcuts import render
from .models import Store
import json
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def shop(request):
    
    name=''
    startp =''
    endp = ''
    if 'product' in request.GET:
		
        name = request.GET['product']
        startp = request.GET['startp']
        endp = request.GET['endp']
        if startp=='' and endp=='':
            shop_list = Store.objects.filter(title__icontains=name).order_by('price')
        else:
            shop_list = Store.objects.filter(title__icontains=name,price__gte=startp,price__lte=endp)
    else:
        shop_list = Store.objects.all().order_by('price')
	
    paginator = Paginator(shop_list,5)
    page = request.GET.get('page')
	
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
		
    content = {'shop_list':contacts,'product':name,'startp':startp,'endp':endp}
    return render(request,'shop.html',content)

def index(request):
    return render(request,'index.html')
