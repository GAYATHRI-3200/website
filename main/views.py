from django.shortcuts import render
from main.forms import contactForm
from . import autoreply
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.	
from django.shortcuts import reverse, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from blog.models import *
from blog.forms import *
# Homepage
def index(request):
    posts = BlogPost.objects.all()
    #return render(request, 'blog/blog.html',{ 'post': posts})
    return render(request, 'main/index.html', { 'post': posts})

def port(request):
    return render(request, 'main/portfolio.html')


def soon(request):
    return render(request, 'main/coming-soon.html')    

def email_template(request):
    return render(request, 'main/email-template.html')

def search_result(request):
    return render(request, 'main/search-results.html')

def port_view(request):
    return render(request, 'main/portfolio-single.html')

def team(request):
    return render(request, 'main/team.html')

def team_view(request):
    return render(request, 'main/team-single.html')
    
def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def service_view(request):
    return render(request, 'main/services-single.html')  

def faq(request):
    return render(request, 'main/faq.html')

def timeline(request):
    return render(request, 'main/timeline.html')

def error(request):
    return render(request, 'main/404.html')              

def contact(request):
    """about page"""
    title = "Contact"
    form = contactForm(request.POST or None) #form handling by view.
    confirmation = None

    if form.is_valid():
        user_name = form.cleaned_data['Username']
        user_message = form.cleaned_data['Message']
        emailsub = user_name + " tried contacting you on TOP5PACKERSANDMOVERS ."
        emailFrom = form.cleaned_data['UserEmail']
        emailmessage = '%s %s user email: %s' %(user_message, user_name, emailFrom)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(emailsub, emailmessage, emailFrom, list(emailTo), fail_silently=True)
        #Autoreply.
        autoreply.autoreply(emailFrom)
        title = "Thanks."
        confirmation = "We will get right back to you."
        form = None

    context = {'title':title, 'form':form, 'confirmation':confirmation,}
    template = 'contact.html'
    return render(request, 'main/contact.html',context)      

