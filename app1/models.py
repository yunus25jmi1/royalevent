from django.db import models

# Create your models here.
class registration(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=80)
	message=models.CharField(max_length=80)
	
	class Meta:
		db_table="registration"
		
		
class menu(models.Model):
	name=models.CharField(max_length=100)
	pic=models.ImageField(upload_to='menu/')
	class Meta:
		db_table="menu"
	def __str__(self):
		return self.name
		
class booking(models.Model):
	name=models.CharField(max_length=100)
	phone=models.CharField(max_length=50)
	email=models.CharField(max_length=80)
	event=models.CharField(max_length=40)
	persons=models.CharField(max_length=60)
	venue=models.CharField(max_length=80)
	time=models.CharField(max_length=80)
	date=models.CharField(max_length=80)
	pic=models.ImageField(upload_to='img/',default="")
	class Meta:
		db_table="booking"
	
		