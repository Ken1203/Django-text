from django.contrib import admin

# Register your models here.
from djangoClassapp.models import BookInfo,pocketInfo

class BookInfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'btitle', 'bpub_date']
	
admin.site.register(BookInfo, BookInfoAdmin) # 修改之前定義的bookinfo 將class名稱放入

class pocketInfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'pname','pgender','pcomment']

admin.site.register(pocketInfo,pocketInfoAdmin)