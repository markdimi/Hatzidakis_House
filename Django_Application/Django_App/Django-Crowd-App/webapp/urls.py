from django.conf.urls import url   #kathorizw url pattern
from .import views #dinamika ginetai import twn viwes apo to topiko paketo


urlpatterns= [
   url(r'^$', views.index, name='index'), 
   url(r'^contact/$', views.contact, name='contact'), 
   url(r'^FutureTasks/$', views.FutureTasks, name='FutureTasks'),

#epistrefei ti sinartisi entos tu arxeiou views tou idiou paketou

]
