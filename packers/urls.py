#from django.conf.urls import path
from django.urls import path
from . import views
app_name = 'packers'

urlpatterns = [  
    path('packers-and-movers-bangalore/', views.bangalore, name='bangalore'),

       
]
