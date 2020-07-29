#from django.conf.urls import path
from django.urls import path
from user import views
from django.contrib.auth.views import LoginView
#app_name = 'user'

urlpatterns = [	
    path('signup/', views.registration_view, name='signup'),
    #path('login/', views.LoginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),   
]
