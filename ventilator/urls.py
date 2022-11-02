from django.conf import settings
from django.urls import URLPattern, path
from . import views

urlpatterns= [ 
    path('',views.index,name='index'),
    path('department',views.department,name='department'),
    path('doctors',views.doctors,name='doctors'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

]
