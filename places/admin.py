from django.contrib import admin
from places.models import Places

class PlacesAdmin(admin.ModelAdmin):
    list_display=('country','company')

admin.site.register(Places,PlacesAdmin)
