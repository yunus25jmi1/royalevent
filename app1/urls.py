from django.urls import path, include
from app1 import views
urlpatterns = [
	path('',views.homeview.as_view()),
	path('home/',views.formview.as_view()),
	path('m1/',views.m1view.as_view()),
	path('contacts/',views.contactsview.as_view()),
	path('jq1/',views.jq1view.as_view()),
	path('services/',views.servicesview.as_view()),
	path('aboutus/',views.aboutusview.as_view()),
	path('jq2/',views.jq2view.as_view()),
	path('menu/',views.menuview.as_view()),
	path('portfolio/',views.portfolioview.as_view()),
	path('blog/',views.blogview.as_view()),
	path('booking/',views.bookingview.as_view()),
	path('insertbooking/',views.insertbooking),
	path('insertform/',views.insertform),
]




