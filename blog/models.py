from django.db import models

# Create your models here.

#django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

def upload_location(instance, filename, **kwargs):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id), title=str(instance.title), filename=filename
		)
	return file_path

class BlogPost(models.Model):
	title 						= models.CharField(max_length=50, null=False, blank=False)	
	body						= RichTextField()
	#image 						= models.ImageField(null=True, blank=False)
	#image 						= models.FileField(upload_to='upload_location', blank=True)
	image 						= models.ImageField(upload_to='post_image', null=False, blank=False)		
	date_published 				= models.DateTimeField(auto_now_add=True, verbose_name="data published")
	date_updated 				= models.DateTimeField(auto_now=True, verbose_name="data updated")
	author 						= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Slug						= models.SlugField(blank=True, unique=True)

	class Meta:
		ordering = ['-date_published']

	def __str__(self):
		return self.title
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url	
class Comment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    reply = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="data created")
    active = models.BooleanField(default=False)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    class Meta:
        ordering = ['created_on']

    def __str__(self):
    	#return 'Comment By {}'.format(self.Name)
        return 'Comment by {}'.format(self.name)
