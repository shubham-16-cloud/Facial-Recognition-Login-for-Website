from django.shortcuts import render
from django.http import HttpResponse
from .models import banner,events,news,about

# Create your views here.
def index(request):
    if request.method == "GET":
        banner_obj = banner.objects.latest('dateofinsert')
        events_obj = events.objects.all()[:4]
        news_obj = news.objects.all()[:6]
        about_obj = about.objects.all()
        return render(request,'index.html',{'banner':banner_obj,'events':events_obj,'news':news_obj,'about':about_obj})
    else:
        return HttpResponse("error")


def info(request, id1):
    if id1 == "event":
        i1 = events.objects.all()
        id = id1
    elif id1 == "news":
        i1 = news.objects.all()
        id = id1
    else:
        i1 =news.objects.filter(id = id1)
        id = "news"

    return render(request,'info.html',{'info':i1,'id':id})