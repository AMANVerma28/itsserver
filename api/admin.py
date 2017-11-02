from django.contrib.gis import admin
from .models import *

# Register your models here.

#Open Street Maps GeoModel Admin is used.
admin.site.register(Household,admin.GeoModelAdmin)
admin.site.register(Member,admin.GeoModelAdmin)
admin.site.register(Farm,admin.GeoModelAdmin)
admin.site.register(Crop,admin.GeoModelAdmin)
admin.site.register(Season,admin.GeoModelAdmin)
admin.site.register(Well,admin.GeoModelAdmin)
admin.site.register(Yield,admin.GeoModelAdmin)
admin.site.register(Storage,admin.GeoModelAdmin)