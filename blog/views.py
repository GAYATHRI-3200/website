from django.shortcuts import render
from django.shortcuts import reverse, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import *
from .forms import *

def blog(request):
	posts = BlogPost.objects.all()
	return render(request, 'blog/blog.html',{ 'post': posts})

def reply(request):
    return render(request, 'blog/reply.html',{})

def sblog(request, slug):
    template_name = 'blog/blog-single.html'
    post = get_object_or_404(BlogPost, Slug = slug)
    #post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


