from django import forms
from app1.models import registration,booking

class registrationform(forms.ModelForm):
	name=forms.CharField(max_length=100)
	phone=forms.CharField(max_length=15)
	email=forms.CharField(max_length=80)
	course=forms.CharField(max_length=50)
	class Meta:
		model=registration
		fields='_all_'
		
class bookingform(forms.ModelForm):
	name=forms.CharField(max_length=100)
	phone=forms.CharField(max_length=15)
	email=forms.CharField(max_length=80)
	event=forms.CharField(max_length=40)
	persons=forms.CharField(max_length=60)
	venue=forms.CharField(max_length=80)
	time=forms.CharField(max_length=80)
	date=forms.CharField(max_length=80)
	pic=forms.ImageField(upload_to='img/',default="")
	class Meta:
		model=booking
		fields='_all_'
				