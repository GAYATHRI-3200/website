#from django.conf.urls import path
from django.urls import path
from . import views
app_name = 'ecommerce'

urlpatterns = [  
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('ecommerce-single/', views.ecommerce_single, name='ecommerce-single'),
    path('ecommerce-cart/', views.ecommerce_cart, name='ecommerce-cart'),   
]
