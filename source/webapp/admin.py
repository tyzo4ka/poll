from django.contrib import admin
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_date']
    list_filter = ['question']
    list_display_links = ['pk', 'question']
    search_fields = ['question']
    exclude = []
    readonly_fields = ['created_date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
