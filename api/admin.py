from django.contrib import admin
from .models import Activity, Stat
# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'title']


class StatAdmin(admin.ModelAdmin):
    list_display = ['activity_id', 'stat', 'timestamp']

admin.site.register(Stat, StatAdmin)
admin.site.register(Activity, ActivityAdmin)
