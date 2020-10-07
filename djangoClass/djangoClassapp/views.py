from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from djangoClassapp.models import BookInfo
# def index(request):
# 	return HttpResponse("hello world!")

def index(request):

	booklist= BookInfo.objects.all()
	
	# 使用 locals()傳遞所有的區域變數
	return render(request,"index.html",locals())

def detail(reqeust, bid):
	#根據圖書編號對應圖書
	book = BookInfo.objects.get(id = int(bid))

	#查尋bookinfo中的所有寶貝信息
	pockets = book.pocketinfo_set.all()
	
	#將圖書信息傳遞到模板中，然後渲染模板
	return render(reqeust,'detail.html',locals())