from djangoClassapp import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('<bid>/',views.detail),
]