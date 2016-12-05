from django.contrib import admin

# Register your models here.

from .models import Document, Recommendation, PickleObject

class DocumentAdmin (admin.ModelAdmin):

    list_display = ('docfile', 'pub_date', 'recent_published')
    list_filter = ['docfile', 'pub_date']
    search_fields=['pub_date']

class RecommendationAdmin (admin.ModelAdmin):

	list_display = ('repstatus', 'pub_date')
	list_filter = ['repstatus', 'pub_date']
	search_fields = ['repstatus', 'pub_date']

class PickleObjectAdmin (admin.ModelAdmin):
    
    list_display = ('args', 'name')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Document,DocumentAdmin)
admin.site.register(Recommendation,RecommendationAdmin)
admin.site.register(PickleObject,PickleObjectAdmin)

