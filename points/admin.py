from django.contrib import admin
from points.models import Points

class PointsAdmin(admin.ModelAdmin):
    list_display=['title',]

admin.site.register(Points,PointsAdmin)
