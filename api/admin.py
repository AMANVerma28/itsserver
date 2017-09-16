from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Household,admin.OSMGeoAdmin)
admin.site.register(Member,admin.OSMGeoAdmin)
admin.site.register(Farm,admin.OSMGeoAdmin)
admin.site.register(Crop,admin.OSMGeoAdmin)
admin.site.register(Well,admin.OSMGeoAdmin)
admin.site.register(Yield,admin.OSMGeoAdmin)