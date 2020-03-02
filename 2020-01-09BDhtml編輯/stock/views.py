from django.shortcuts import render
from .models import Stock
import json

# Create your views here.
def stock(request):
    if 'no' in request.GET:
        noid = request.GET['no']
        shop_list = Stock.objects.filter(no=noid).order_by('id')
    else:
        shop_list = Stock.objects.all()
    group = Stock.objects.values('no').distinct()
    
    content = {'shop_list':shop_list,'group':group}
    return render(request,'stock.html',content)

def charts(request):
    stock_list=Stock.objects.filter(no=2330).order_by('-id')
    data=[]
    alldate=[]
    for i in stock_list:
        data.append(float(i.closeprice))
        date_time=i.create_date.strftime("%y/%m/%d")
        alldate.append(date_time)
    content={'listdata':data}
    return render(request,'getChart.html',content)