from django.shortcuts import render
from .models import Message
import datetime
# Create your views here.
def message(request):
    
    
    if 'title' in request.POST:
        title = request.POST['title']
        name = request.POST['username']
        content = request.POST['content']
        dt = datetime.datetime.now()
        Message.objects.create(title=title,name=name,content=content,create_date=dt)
    
    
    return render(request,'message.html')