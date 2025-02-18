from django.contrib import admin
from welcome.models import pages
# Register your models here.
class pagesAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
admin.site.register(pages,pagesAdmin)
