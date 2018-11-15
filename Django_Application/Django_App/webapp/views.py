from django.shortcuts import render
#from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'webapp/home.html') 

def contact(request):
	return render(request, 'webapp/basic.html', {'content':['Για να επικοινωνήσετε με τους δημιουργούς του ιστότοπου μπορείτε να στείλετε ηλεκτρονικό μήνυμα στις παρακάτω διευθύνσεις:']}) #περναω ενα λεξικο με 1 string
	
def FutureTasks(request):
	return render(request, 'webapp/basic2.html',{'content2':['Η παρούσα ενότητα βρίσκεται υπό κατασκευή!']})
#return HttpResponse ("<h2>γεια</h2>")
