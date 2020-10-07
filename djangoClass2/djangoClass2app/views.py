# from django.shortcuts import render ,redirect
# #引入models
# from djangoClass2app.models import *
# from datetime import date

# def index(request):
# 	#查詢所有圖書
# 	booklist = BookInfo.objects.all()
# 	#將圖書列表傳遞到模板中，然後渲染模板
# 	return render(request,"index.html",locals())
	
# #建立新百科
# def create(request):
# 	book=BookInfo()
# 	book.btitle = '宇宙百科'
# 	book.bpub_date = date(2020,1,30)
# 	book.save()
# 	#到首頁
# 	return redirect('/')

# #刪除指定的百科
# def delete(request,id):
# 	book=BookInfo.objects.get(id=int(id))
# 	book.delete()
# 	#到首頁
# 	return redirect('/')

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# def index(request):
# 	return HttpResponse("views Test")
def index(request):
 	return render(request,"index.html")

def show(request,id):
	return HttpResponse('show id : {}'.format(id))

def method_show(request):
	return HttpResponse(request.method)

def show_reqarg(request):
	if request.method == 'GET':
		a = request.GET.get('a') #獲取請求參數a
		b = request.GET.get('b') #獲取請求參數b
		c = request.GET.get('c') #獲取請求參數c
		return render(request, 'show_getarg.html', {'a':a, 'b':b, 'c':c})
	else:
		name = request.POST.get('name') #獲取name
		gender = request.POST.get('gender') #獲取gender
		hobbys = request.POST.getlist('hobby') #獲取hobby
		return render(request, 'show_postarg.html', {'name':name, 'gender':gender, 'hobbys':hobbys})
    
def index2(request):
	str1='<h1>hello world</h1>'
	return HttpResponse(str1)


def index3(request):

	return render(request, 'index3.html', {'h1': 'hello'})
	# #加載模板
	# t1=loader.get_template('index3.html')
	
	# #構造上下文
	# context={'h1':'hello'}
	
	# #使用上下文渲染模板，生成字符串後回應
	# return HttpResponse(t1.render(context))
def json1(request):
	return render(request,'json.html')

def json2(request):
    dic = {'h1':'hello','h2':'world'}
    return JsonResponse(dic)

# def red1(request):
# 	return HttpResponseRedirect('/')

def red1(request):
	return redirect('/')
import json #使用json dump and load 解決cookie無法儲存utf8的問題
def cookie_set(request):
	response = HttpResponse("<h1>設置Cookie，請查看 response header</h1>")
	response.set_cookie('h1', json.dumps('你好'))
	return response

def cookie_get(request):
	response = HttpResponse("讀取Cookie，數據如下：<br>")
	if 'h1' in request.COOKIES:
		response.write('<h1>' + json.loads(request.COOKIES['h1']) + '</h1>')
	return response

def session_test(request):
    #request.session['h1']='hello'
    # h1=request.session.get('h1')
    # return HttpResponse(h1)
	#return HttpResponse('寫入session')
    # del request.session['h1']
    # return HttpResponse('ok')
    request.session.flush()
    return HttpResponse('ok')
from djangoClass2app.models import BookInfo

def temp_inherit(request):
	context={'title':'模板繼承','list':BookInfo.objects.all()}
	return render(request,'temp_inherit.html',context)