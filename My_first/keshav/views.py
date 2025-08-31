from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import Tweetform
from django.contrib.auth import login
from .forms import SignUpForm, BlogForm
from .models import MoreDetails



# this is import for connection or making the logic of buttons and pages...

def tweet_list(request):
    tweets = Message.objects.all().order_by('-created_at')
    return render (request,'tweet/tweet_list.html',{'tweet': tweets})

# this is the user of decorators to guest user.
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = Tweetform()
        return render (request, 'tweet/tweet_form.html',{'form':form})
    

@login_required    
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Message,pk=tweet_id, user= request.user)
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES,instance=tweet)
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
        
    else:
        form = Tweetform()
        return render (request,'tweet/create_tweet.html',{'form': form})
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Message,pk=tweet_id, user = request.user)
    if request.method == 'POST':
        # not valid for required
        tweet.delete()
        return redirect('tweet_list')
    return render (request,'tweet/tweet_delete.html',{'tweet': tweet})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm((request.POST))
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = SignUpForm()
    return render(request,'registration/register.html', {'form': form})

def more(request):
    return render(request,'tweet/more_')

      # this method is used to clean the data and this is django built in tools
     # user.set_password(form.cleaned_data['password1'])
     # user.save()

def blog_list(request):
    blogs = MoreDetails.objects.all().order_by('-created_at')
    return render(request,'tweet/blog_list.html',{'blogs': blogs})

def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        
        else:
            form = BlogForm()
        return render(request,'tweet/blog_form.html',{'form': form})





