from django.contrib import admin

# Register your models here.

from .models import *

class IELTSAdmin(admin.ModelAdmin):
    list_display = ['family_name','overal','cefr_level']
    list_per_page = 10
    search_fields = ['family_name','overal', 'cefr_level']
    class Meta:
        model = IELTS
admin.site.register(IELTS,IELTSAdmin)
