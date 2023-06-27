from django.shortcuts import render
from django.http import HttpResponse
# importing models
from App.models import *
# importing length function
from django.db.models.functions import Length

# Create your views here.
def show_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'show_topic.html',d)

def show_webpage(request):
    LWO=Webpage.objects.all()    
    d={'LWO':LWO}
    return render(request,'show_webpage.html',d)

def show_record(request):
    LAO=AccessRecord.objects.all()
    d={'LAO':LAO}
    return render(request,'show_record.html',d)

def update_content(request):
    # using update method
    # 1 row satisfying
    Webpage.objects.filter(name='Peace').update(url='http://peaceful.com')
    # multiple rows satisfying condition
    Webpage.objects.filter(topic_name='Rugby').update(url='https://Django.ac.in')
    # No rows satisfying
    Webpage.objects.filter(name='Naguru').update(topic_name='SQL')
    # using update_or_create method
    
    TO=Topic.objects.get(topic_name='Hockey')
    # 1 row satisfying
    Webpage.objects.update_or_create(name='George',defaults={'topic_name':TO}) 
    # multiple rows satisfying condition
    # Webpage.objects.update_or_create(topic_name=TO,defaults={'name':'SYERAA007'}) #Error
    # No rows satisfying
    DO=Topic.objects.get(topic_name='Django')
    Webpage.objects.update_or_create(name='Hockey',defaults={'topic_name':DO,'url':'https://DjnagoFW.in'}) 
    
    
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'show_webpage.html',d)

def delete_content(request):
    AccessRecord.objects.filter(author='Shyamala').delete()
    

    LAO=AccessRecord.objects.all
    d={'LAO':LAO}
    return render(request,'show_record.html',d)