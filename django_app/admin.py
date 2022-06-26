from django.contrib import admin
from .models import Words,Admins,Users
# Register your models here.

class uers(admin.ModelAdmin):
    list_display = ['full_name','xabar','sana']
    readonly_fields = ['full_name','xabar','sana','telegram_id','kanal']
    list_filter = ['sana','kanal']
    search_fields = ['full_name','telegram_id']


admin.site.register(Words)
admin.site.register(Admins)
admin.site.register(Users,uers)