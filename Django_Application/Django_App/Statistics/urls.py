from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from Statistics.models import SensorMeasurement

#-date ωστε να ειναι descending με τις πιο προσφατες ημερμονηνιες να ειναι πρωτες
	#[τιμη] ειναι οριο εμφανισης

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=SensorMeasurement.objects.all().order_by("-date")[:30],template_name="Statistics/Statistics.html")),

	#url(r'^(?P<pk>\d+)$', DetailView.as_view(model=SensorMeasurement, template_name="Statistics/allmeasurements.html"))
 ]
	
