from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from pusher import Pusher
pusher = Pusher(app_id=u'1161784', key=u'fc008af4d5debaaadd5e', secret=u'89e8510181b8e81c225a', cluster=u'us2')
import json
from .models import Feed
from .forms import DocumentForm

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

@login_required
def index(request):
        # get all current photos ordered by the latest
        all_documents = Feed.objects.all().order_by('-id')
        # return the index.html template, passing in all the feeds
        return render(request, 'feed.html', {'all_documents': all_documents})

#function that authenticates the private channel 
def pusher_authentication(request):
        channel = request.GET.get('channel_name', None)
        socket_id = request.GET.get('socket_id', None)
        auth = pusher.authenticate(
          channel = channel,
          socket_id = socket_id
        )
        return JsonResponse(json.dumps(auth), safe=False)
#function that triggers the pusher request
def push_feed(request):
        # check if the method is post
        if request.method == 'POST':
            # try form validation
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save()
                # trigger a pusher request after saving the new feed element 
                pusher.trigger(u'a_channel', u'an_event', {u'description': f.description, u'document': f.document.url})
                return HttpResponse('Image uploaded ! Go to /feed to see your feed :)')
            else:
                # return a form not valid error
                return HttpResponse('form not valid')
        else:
            # return error, type isnt post
           return HttpResponse('error, please try again')
