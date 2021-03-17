from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comments, Like
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import json
# Create your views here.
def login(request, user):
  return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

@login_required
def home(request):
  return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class PostListView(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 10
  def get_context_data(self, **kwargs):
		        context = super(PostListView, self).get_context_data(**kwargs)
		        if self.request.user.is_authenticated:
			              liked = [i for i in Post.objects.all() if Like.objects.filter(user = self.request.user, post=i)]
			              context['liked_post'] = liked
		        return context

class UserPostListView(LoginRequiredMixin, ListView):	
  model = Post
  template_name = 'feed/user_posts.html'
  context_object_name = 'posts'
  paginate_by = 10

  def get_context_data(self, **kwargs):		
    context = super(UserPostListView, self).get_context_data(**kwargs)
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    liked = [i for i in Post.objects.filter(user_name=user) if Like.objects.filter(user = self.request.user, post=i)]
    context['liked_post'] = liked
    return context	
  
  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(user_name=user).order_by('-date_posted')

@login_required
def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  user = request.user
  is_liked =  Like.objects.filter(user=user, post=post)
  if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():			
          data = form.save(commit=False)
          data.post = post
          data.username = user
          data.save()
          return redirect('post-detail', pk=pk)
  else:
        form = NewCommentForm()
  return render(request, 'post_detail.html',{'post':post, 'is_liked':is_liked, 'form':form})

@login_required
def create_post(request): ## this is for posting a picture
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.user_name = user
			data.save()
			messages.success(request, f'Posted Successfully')
			return redirect('home')
	else:
		form = NewPostForm()
	return render(request, 'createPost.html', {'form':form})

@login_required ## to delete a picture
def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	if request.user== post.user_name:
		Post.objects.get(pk=pk).delete()
	return redirect('home') 
