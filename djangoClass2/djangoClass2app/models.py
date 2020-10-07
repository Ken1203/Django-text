# from django.db import models

# class BookInfo(models.Model):
# 	btitle = models.CharField(max_length=20)
# 	bpub_date = models.DateField()
# 	bread = models.IntegerField(default=0)
# 	bcomment = models.IntegerField(default=0)
# 	isDelete = models.BooleanField(default=False)

# class pocketInfo(models.Model):
# 	pname = models.CharField(max_length=20)
# 	pgender = models.BooleanField()
# 	pcomment = models.CharField(max_length=100)
# 	pbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
# 	isDelete = models.BooleanField(default=False)

from django.db import models
# Create your models here.

class BookInfo(models.Model):
	# btitle = models.CharField(max_length=20)
	btitle = models.CharField(max_length=20,db_column='title')
	bpub_date = models.DateField()
	bread = models.IntegerField(default=0)
	bcomment = models.IntegerField(default=0)
	isDelete = models.BooleanField(default=False)#刪除

class pocketInfo(models.Model):
	pname = models.CharField(max_length=20)
	pgender = models.BooleanField()	
	#pcomment = models.CharField(max_length=100)
	pcomment = models.CharField(max_length=200, null=True, blank=False)
	pbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
	isDelete = models.BooleanField(default=False)