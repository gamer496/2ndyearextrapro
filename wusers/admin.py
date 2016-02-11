from django.contrib import admin
from wusers.models import Wusers
from django.contrib.auth.models import User

class WuserAdmin(admin.ModelAdmin):
    list_display=('get_username','get_email')
    def get_username(self,obj):
        return obj.user.username
    def get_email(self,obj):
        return obj.user.email
    get_username.short_description='Username'
    get_username.admin_order_field='Username'
    get_email.short_description='Email'

admin.site.register(Wusers,WuserAdmin)
