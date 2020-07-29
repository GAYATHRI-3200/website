#from django.conf.urls import path
from django.urls import path
from blog import views
app_name = 'blog'

urlpatterns = [  
    path('blog/', views.blog, name='blog'),
    #path('blog-single/', views.sblog, name='blog-single'),
    path('blog-single/<slug:slug>/', views.sblog, name='blog-single'),
    path('reply/', views.reply, name='reply'),
       
]
