from django.db import models

# Create your models here.-basi dedomenwn


class SensorMeasurement(models.Model) :
	#coloumns=datatype(constrains)
	sensor=	models.CharField(max_length=10)
	measurement1=models.CharField(max_length=17)
	measurement2=models.CharField(max_length=5)
	date=models.DateTimeField()


# PositiveSmallIntegerField 0 εως 32767 αν θελουμε-´οριζονται' αρνητικοι τοτε : SmallIntegerField
#https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.IntegerField


def __str__(self):
	return self.sensor
        #return u'%s %s %s' % (self.sensor, self.measurement1, self.measurement2)

	
#για meta-deta το παραπανω θα επιστρεφει μονο αντικειμενα. πχ SensorMeasurement.title δεν επιστρεφει string για αυτο κανω την __str__

