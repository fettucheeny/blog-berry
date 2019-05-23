from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    template = 'list.html'
    posts = Post.objects.all().order_by('-publish_date')
    context = {
    	'posts': posts,
    }
    return render(request, template, context)

def view_post(request, post_id):
	template = 'view_post.html'
	post = Post.objects.get(id=int(post_id))
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
                user=form.cleaned_data["user"],
                text=form.cleaned_data["text"],
                post=post
            )
			comment.save()
	comments = Comment.objects.filter(post=post)
	context = {
			'post': post,
			'comments': comments,
			'comment_form': CommentForm()
			}
	return render(request, template, context)

def add_post(request):
	template = 'add_post.html'
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'post_form':PostForm(),
		}
	return render(request,template,context)

def edit_post(request, post_id):
	template = 'edit_post.html'
	post = Post.objects.get(id=int(post_id))
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'post_form': PostForm(instance=post),
		}
	return render(request, template, context)

def delete_post(request, post_id):
	post = Post.objects.get(id=int(post_id))
	post.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))


