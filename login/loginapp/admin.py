from django.contrib import admin

from .models import Account,Review

admin.site.register(Account)

@admin.register(Review)  
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('lab_id', 'lab_name','score1', 'score2', 'score3', 'score4')
    list_display_links = ('lab_name',)
    list_editable = ('score1', 'score2', 'score3', 'score4')