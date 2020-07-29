#from django.conf.urls import path
from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
	path('portfolio/', views.port, name='portfolio'),
    path('portfolio-single/', views.port_view, name='portfolio-single'),
    path('FAQS/', views.faq, name='faq'),
    path('404/', views.error, name='404'),
    path('search-result/', views.search_result, name='search-results'),
    path('timeline/', views.timeline, name='timeline'),
    path('team/', views.team, name='team'),
    path('team-single/', views.team_view, name='team-single'),
    path('services/', views.services, name='services'),
    path('services-single/', views.service_view, name='services-single'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('coming-soon/', views.soon, name='coming-soon'),
    path('email-template/', views.email_template, name='email-template'),
]
