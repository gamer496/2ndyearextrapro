from django.contrib import admin
from contactmeans.models import Messages

# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display=('message',)
admin.site.register(Messages,MessagesAdmin)
