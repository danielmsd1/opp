from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
	path('',views.home, name='home'),
	path('home',views.home, name='home'),
	path('portfolioview/<int:project_id>', views.portfolioview, name='portfolioview'),
	path('newsletter', views.newsletter,name='newsletter'),
	path("subscription", views.subscription, name="subscription"),
]