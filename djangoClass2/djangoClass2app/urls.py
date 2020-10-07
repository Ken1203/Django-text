# from django.conf.urls import url
# from djangoClass2app import views
# from django.urls import path

# urlpatterns=[

# 	path('',views.index),
#     path('delete/<id>',views.delete),
# 	path('create',views.create),

# ]
from django.conf.urls import url #導入url函數
from djangoClass2app import views #導入視圖
from django.urls import path

urlpatterns = [
    path('', views.index), #建立url和views.index函數的關聯
    path('delete/<id>/', views.show),
    path('method_show/', views.method_show),
    path('show_reqarg/', views.show_reqarg),
    path('index2/', views.index2),
    path('index3/',views.index3),
    path('json1/', views.json1),
    path('json2/', views.json2),
    path('red1/', views.red1),
    path('cookie_set/',views.cookie_set),
    path('cookie_get/',views.cookie_get),
    path('session_test/',views.session_test),
    path('temp_inherit/', views.temp_inherit),
]