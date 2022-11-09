from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tb_news
# Create your views here.


def index(request):

    return render(request, 'mywebsite/index.html')


def addnews(request):
    return render(request, 'mywebsite/addnews.html')


def result(request):
    name = request.POST['name_news']
    detail = request.POST['name_detail']
    mydata = {
        'name_news': name,
        'name_detail': detail
    }
    print(name)
    return render(request, 'mywebsite/result.html', mydata)


def addnewsdata(request):
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_photo = request.FILES['news_photo']
    content = tb_news(news_title=news_title,
                      news_detail=news_detail, news_photo=news_photo)
    content.save()
    return redirect("/contentmanager")


def contentmanager(request):
    mydatanews = tb_news.objects.all()
    return render(request, 'mywebsite/contentnewsmanager.html', {'news': mydatanews})
