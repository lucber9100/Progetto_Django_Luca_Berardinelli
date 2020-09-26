from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from datetime import datetime
from django.contrib import messages

# -------- Ex.1 + Ex.7
def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # create user
            cleaned_data = form.cleaned_data
            form = form.save(commit=False)
            username = cleaned_data.get('username')
            raw_password = cleaned_data.get('password1')
            is_admin = cleaned_data.get('is_admin')
            if is_admin == True:
                form.is_staff = True
                form.is_superuser = True
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logged_in(request)
            return render(request, 'api/home.html', {})
    else:
        form = SignUpForm()
    return render(request, 'api/home.html', {'form': form, 'user': request.user})

# -------- Ex.2
def new_post(request):
     posts_list = Post.objects.all()
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             if 'hack' in form.cleaned_data['content']:
                 messages.info(request, 'You cannot create a post containing the word \'hack\'')
                 return render(request, 'api/post_edit.html', {'form': form, 'posts': posts_list})
             else:
                 post = form.save(commit=False)
                 post.user = request.user
                # post.writeOnChain()
                 post.save()
                 return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
         return render(request, 'api/post_edit.html', {'form': form, 'posts': posts_list})

# -------- Ex.3
def admin_panel(request):
    posts_list = Post.objects.filter().order_by('user')
    user_curr = ''
    count = 0
    posts = []
    for post in posts_list:
        if user_curr != post.user:
            if user_curr != '':
                posts.append({'user' : user_curr, 'posts' : count})
            # reset temp variables
            user_curr = post.user
            count = 0
        count += 1
    posts.append({'user': user_curr, 'posts': count})

    postslist = Post.objects.filter().order_by('-user')
    return render(request, 'api/admin_panel.html', {'posts' : posts,  'postslist': postslist})

# -------- Ex.4
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'api/user_detail.html', {'user': user})

# -------- Ex.5
def posts1h(request):
    response = []
    posts = Post.objects.filter()
    for post in posts:
        post_dt = post.datetime.replace(tzinfo=None)
        delta = datetime.now() - post_dt
        if(((delta).seconds/60) <= 60):
            response.append({
                'datetime' : post.datetime,
                'content' : post.content,
                'author' : f"{post.user.first_name} {post.user.last_name}"
            })
    return JsonResponse(response, safe=False)

# -------- Ex.6
def get_occurrences(request, string):
    response = []
    response.append({
        'occurrences of ' + string : Post.objects.filter(content__icontains=string).count()
    })
    return JsonResponse(response, safe=False)

# -------- Ex.8
def logged_in(request):
    # retrieve IP and store in Redis
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
       ip = x_forwarded_for.split(',')[0]
    else:
       ip = request.META.get('REMOTE_ADDR')

    # check previous user ip
    user = UserIpLog.objects.filter(user=request.user)
    if not user:
        UserIpLog.objects.create(user=request.user, ip=ip)
    elif user[0].ip != ip:
        UserIpLog.objects.filter(user=request.user).update(ip=ip)
        messages.info(request, f'Your IP is changed | Old IP={user[0].ip} -> New IP={ip}')
    return render(request, 'api/home.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts_list = Post.objects.filter().order_by('datetime')
    return render(request, 'api/post_detail.html', {'post': post, 'posts': posts_list})



