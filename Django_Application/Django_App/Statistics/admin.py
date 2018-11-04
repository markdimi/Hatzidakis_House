from django.contrib import admin
from Statistics.models import SensorMeasurement

# Register your models here.

class SensorMeasurementAdmin(admin.ModelAdmin):
	list_display = ('sensor', 'measurement1', 'measurement2','date')
  


admin.site.register(SensorMeasurement,SensorMeasurementAdmin)

