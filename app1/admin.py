from django.contrib import admin
from app1.models import registration, menu, booking

# Register your models here.

@admin.register(registration)
class registrationAdmin(admin.ModelAdmin):
	list_display=('name','email','message',)

@admin.register(menu)
class menuadmin(admin.ModelAdmin):
	pass
	
@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
	list_display=('name','phone','email','event','persons','venue','time','date','pic',)

