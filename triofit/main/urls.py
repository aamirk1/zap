from django.urls import path
from . import views
from main.controller import pages
urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus',pages.aboutus,name='aboutus'),
    path('gallery',pages.gallery,name='gallery'),
    path('tpm',pages.ThirdPartyManufac,name='tpm'),
    path('contactus',pages.contactus,name='contactus'),
]
