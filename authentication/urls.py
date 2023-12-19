from django.urls import path
from . import views


urlpatterns = [
    # pages
    path('', views.home, name = 'home'),
    path('EDS - Contact Us', views.contact, name = 'contact'),
    path('EDS - About Us', views.aboutus, name = 'aboutus'),
    path('EDS - Ourservices', views.ourservices, name = 'ourservices'),

    # algorithms
]


