from django.db import models

# Create your models here.


class BookInfo(models.Model):
	btitle = models.CharField(max_length=20) #varchart(20)
	bpub_date = models.DateField() #date


class pocketInfo(models.Model):
	pname = models.CharField(max_length=20)
	pgender = models.BooleanField()
	pcomment = models.CharField(max_length=100)
	pbook = models.ForeignKey('bookInfo',on_delete=models.CASCADE)