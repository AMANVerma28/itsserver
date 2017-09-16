from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^household/$',views.householddetail),
	url(r'^member/',views.memberdetail),
	url(r'^farm/',views.farmdetail),
	url(r'^crop/',views.cropdetail),
	url(r'^well/',views.welldetail),
	url(r'^wellwater/',views.yielddetail),
    url(r'^household/(?P<dat_id>[0-9]+)/',views.housedetail),
    url(r'^householdall/',views.HouseholdALL),
]