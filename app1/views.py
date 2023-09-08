from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from app1.forms import registrationform, bookingform
from app1.models import menu
from app1.models import booking
# Create your views here.

class homeview(TemplateView):
	template_name="home.html"
class formview(TemplateView):
	template_name="form1.html"
class m1view(TemplateView):
	template_name="m1.html"
class contactsview(TemplateView):
	template_name="contacts.html"
class jq1view(TemplateView):
	template_name="jq1.html"
class servicesview(TemplateView):
	template_name="services.html"
class aboutusview(TemplateView):
	template_name="aboutus.html"
class jq2view(TemplateView):
	template_name="jq2.html"
class menuview(TemplateView):
	template_name="menu.html"
class portfolioview(TemplateView):
	template_name="portfolio.html"
class blogview(TemplateView):
	template_name="blog.html"
class bookingview(TemplateView):
	template_name="booking.html"
class menuview(ListView):
	template_name="menu.html"
	def get_queryset(self):
		return menu.objects.all()

def insertform(request):
	if request.method=='POST':
		form=registrationform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contacts/')
	else:
		form=registrationform()
	return render(request,"contacts.html",{'form':form})
			
def insertbooking(request):
	if request.method=='POST':
		form=bookingform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/booking/')
	else:
		form=bookingform()
		return render(request,"booking.html",{'form':form})
			