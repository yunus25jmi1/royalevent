from django import forms
from app1.models import registration, booking

class registrationform(forms.ModelForm):
	name=forms.CharField(max_length=100)
	email=forms.CharField(max_length=80)
	message=forms.CharField(max_length=80)
	
	class Meta:
		model=registration
		fields='__all__'
		
class bookingform(forms.ModelForm):
	name=forms.CharField(max_length=100)
	phone=forms.CharField(max_length=50)
	email=forms.CharField(max_length=80)
	event=forms.CharField(max_length=40)
	persons=forms.CharField(max_length=60)
	venue=forms.CharField(max_length=80)
	time=forms.CharField(max_length=80)
	date=forms.CharField(max_length=80)
	pic=forms.ImageField()
	class Meta:
		model=booking		
		fields='__all__'