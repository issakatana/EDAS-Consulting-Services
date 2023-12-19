from django.urls import path
from . import views


urlpatterns = [
    # pages
    path('', views.home, name = 'home'),
    path('EDS - Contact Us', views.contact, name = 'contact'),

    # algorithms
]


