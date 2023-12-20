from django.urls import path
from . import views


urlpatterns = [
    # pages
    path('', views.home, name = 'home'),
    path('EDS - About Us', views.aboutus, name = 'aboutus'),
    path('EDS - Ourservices', views.ourservices, name = 'services'),
    path('EDS - Career Management', views.careermanagement, name = 'careermanagement'),
    path('EDS - We Are Hiring', views.wearehiring, name = 'wearehiring'),
    path('EDS - Blog', views.blog, name = 'blog'),
    path('EDS - Contact Us', views.contact, name = 'contact'),

    # algorithms
]


