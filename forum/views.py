from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SubscribedUser, Posts
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from requests.api import request, request
import json
from django.contrib import messages 


def index(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('Home')
    else:
        flag = 1  # Means user is already Registered
        plan = 0
        try:
            # Raises Exception when user is not already registered
            this_user = SubscribedUser.objects.get(user_name=request.user.username)
            plan = this_user.subsType
        except:
            flag = 0  # Means Exception occured ie. user is not Registered

        params = {
            'flag': flag,
            'plan': plan,
        }
        return render(request, 'forum/forum.html', params)


@login_required(login_url='/')
def post(request):
    # To Register Subscription of New User
    if request.method == 'POST':
        flag = False  # Means user is already Registered
        try:
            # Raises Exception when user is not already registered
            SubscribedUser.objects.get(user_name=request.user.username)
        except:
            flag = True  # Means Exception occured ie. user is not Registered

        if flag == True:
            new_subsUSer = SubscribedUser()
            new_subsUSer.user_name = request.user.username
            new_subsUSer.first_name = request.user.first_name
            new_subsUSer.last_name = request.user.last_name
            new_subsUSer.email = request.user.email
            new_subsUSer.jobTitle = request.POST.get('jobTitle')
            new_subsUSer.bio = request.POST.get('bio')
            new_subsUSer.subsType = int(request.POST.get('subsType'))
            profilePic = request.FILES['profilePic']
            fs = FileSystemStorage()
            fs.save(profilePic.name, profilePic)
            new_subsUSer.profilePic = profilePic.name
            resume = request.FILES['resume']
            fs = FileSystemStorage()
            fs.save(resume.name, resume)
            new_subsUSer.resume = resume.name
            new_subsUSer.portfolio = request.POST.get('portfolio')
            new_subsUSer.save()

    # This Will Show to Newly Registered User as well as already registered User
    current_user = SubscribedUser.objects.get(
        user_name=request.user.username)  # Current User
    followers = current_user.followers.split('$')  # Followers List
    followers.pop()  # Removing Last element of list bcoz it is blank bcoz of split function
    num_followers = len(followers)  # No of Followers
    followings = current_user.followings.split('$')  # Followings List
    followings.pop()  # Removing Last element of list bcoz it is blank bcoz of split function
    num_followings = len(followings)  # No of Followings

    # LOGIC OF SHOWING POSTS OF FOLLOWINGS

    # a=[]                 #List of Dictionaries containing Post and Sender Info
    # for follow in followings:
    #     b={}                #Dictionary containing Post and Sender Info
    #     posts=Posts.objects.filter(sender_id=int(follow)) #follow is user_id of following , Fetching posts of Followings
    #     sender=SubscribedUser.objects.get(user_id=int(follow))
    #     for post in posts:
    #         b['post']=post
    #         b['sender']=sender
    #         a.append(b)
    # # 

    # LOGIC FOR SHOWINGS ALL POSTS OF ALL USERS

    posts = Posts.objects.all()
    list_posts = []  # List of Dictionaries containing Post and Sender Info
    for post in posts:
        sender = SubscribedUser.objects.get(
            user_id=int(post.sender_id))  # Sender Info
        diction = {}  # Dictionary containing Post and Sender Info
        diction['post'] = post
        diction['sender'] = sender
        list_posts.append(diction)
    list_posts.reverse()  # Latest First

    params = {'user': current_user, 'list_posts': list_posts, 'num_posts': len(
        list_posts), 'num_followers': num_followers, 'num_followings': num_followings}

    return render(request, 'forum/posts.html', params)

@login_required(login_url='/')
def createPost(request):
    if request.method == 'POST':
        newPost = Posts()
        newPost.sender_id = int(request.POST.get('sender-id'))
        newPost.content = request.POST.get('content')
        image = request.FILES['create-post-img']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        newPost.image = image.name
        newPost.time = datetime.now()
        newPost.save()

        # To save Post Id in Sender's Object
        sender = SubscribedUser.objects.get(
            user_id=int(request.POST.get('sender-id')))
        sender.posts = str(newPost.post_id) + '$'
        sender.save()

    return redirect(request. META['HTTP_REFERER'])

@login_required(login_url='/')
def profile(request , req_user = None):
    required_user = None
    if request.method == 'POST':
        user_id = request.POST.get('req-user')
        required_user = SubscribedUser.objects.get(user_id=user_id)  # Required User
    elif req_user != None :
        required_user = req_user
    else:
        required_user = SubscribedUser.objects.get(user_name=request.user.username)

    req_followers = required_user.followers.split('$')  # Required User Followers List
    req_followers.pop()  # Removing Last element of list bcoz it is blank bcoz of split function
    num_req_followers = len(req_followers)
    list_followers = []
    for id in req_followers:
        follower = SubscribedUser.objects.get(user_id=int(id))
        list_followers.append(follower)

    req_followings = required_user.followings.split('$')  # Required User Followings List
    req_followings.pop()   # Removing Last element of list bcoz it is blank bcoz of split function
    num_req_followings = len(req_followings)
    list_followings = []
    for id in req_followings:
        following = SubscribedUser.objects.get(user_id=int(id))
        list_followings.append(following)

    req_posts = Posts.objects.filter(sender_id=required_user.user_id)  # Required_user Posts
    req_posts = list(req_posts)
    req_posts.reverse()

    current_user = SubscribedUser.objects.get(user_name=request.user.username)  # Current User
    followings = current_user.followings.split('$')  # Followings List
    followings.pop()  # Removing Last element of list bcoz it is blank bcoz of split function
    followings1 = []
    for follow in followings :
        followings1.append(int(follow))
   
    params = {'req_user': required_user, 'req_posts': req_posts,'num_posts':len(req_posts), 'followers':list_followers,'followings':list_followings,'cur_followings':followings1,'num_followers':num_req_followers,'num_followings': num_req_followings,'cur_user':current_user }

    return render(request, 'forum/profile.html',params)

@login_required(login_url='/')
def follow(request):
    if request.method == "POST":
        other_user_id = request.POST.get('other-user') #User Id of person(Other User) to whom Current User wish to follow
        current_user_id = request.POST.get('current-user') 
        required_user_id = request.POST.get('req-user') # USer ID of User Whose Profile was showing
        required_user = SubscribedUser.objects.get(user_id = required_user_id)
        current_user = SubscribedUser.objects.get(user_id = current_user_id)  #Current User
        followings = current_user.followings.split('$')   
        if other_user_id not in followings :
            current_user.followings += (str(other_user_id)+'$')  # Adding that Other USer in Following List of Current User 
            current_user.save()
            other_user = SubscribedUser.objects.get(user_id = other_user_id) #Other User
            other_user.followers += (str(current_user_id)+'$') #AddingCurrent user in Followers List
            other_user.save()
        return (profile(request,required_user))

@login_required(login_url='/')
def unfollow(request):
     if request.method == "POST":
        other_user_id = request.POST.get('other-user') #User Id of person(Other User) to whom Current User wish to unfollow
        current_user_id = request.POST.get('current-user') 
        required_user_id = request.POST.get('req-user') # USer ID of User Whose Profile was showing
        required_user = SubscribedUser.objects.get(user_id = required_user_id)
        current_user = SubscribedUser.objects.get(user_id = current_user_id) #Current User
        # Removing that Other USer from Following List of Current User 
        string = (str(other_user_id)+'$')
        followings = current_user.followings 
        followings = followings.replace(string,'')
        current_user.followings = followings
        current_user.save()

        other_user = SubscribedUser.objects.get(user_id = other_user_id) #Other User
        # Removing  Current USer from Followers List of Other User 
        string = (str(current_user_id)+'$')
        followers = other_user.followers 
        followers = followers.replace(string,'')
        other_user.followers = followers
        other_user.save()

        return (profile(request,required_user))

@login_required(login_url='/')
def editProfile(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = SubscribedUser.objects.get(user_id=int(user_id))
        try:
            profilePic = request.FILES['profilePic-input']
            fs = FileSystemStorage()
            fs.save(profilePic.name, profilePic)
            user.profilePic = profilePic.name
        except:
            pass

        try:
            resume = request.FILES['resume-input']
            fs = FileSystemStorage()
            fs.save(resume.name, resume)
            user.resume = resume.name
        except:
            pass

        bio = request.POST.get('bio-input')
        if(bio != ''):
            user.bio = bio

        jobTitle = request.POST.get('jobTitle-input')
        if(jobTitle != ''):
            user.jobTitle = jobTitle

        portfolio = request.POST.get('portfolio-input')
        if(portfolio != ''):
            user.portfolio = portfolio

        user.save()
        return redirect(request. META['HTTP_REFERER'],req_user = user_id )

@login_required(login_url='/')
def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        query = query.lower()
        query_list = query.split(' ')
        users = SubscribedUser.objects.all().values() #All Users in Substribed Users
        search_results = []
        for user in users:
            for Query in query_list:
                if Query in user['user_name'].lower() or Query in user['first_name'].lower() or Query in user['last_name'].lower() or Query in user['jobTitle'].lower() :
                    search_results.append(user) 
        if len(search_results) == 0:
            return JsonResponse({'success': False ,'results':search_results})
        else:
            return JsonResponse({'success': True ,'results':search_results})

@login_required(login_url='/')
def payment(request):
    if request.method == 'POST':
        plan = request.POST['plan']
        params = {
            'plan': plan,
        }
    return render(request, 'forum/payment.html', params)


@login_required(login_url='/')
def subscribe(request):
    if request.method == 'POST':
        plan = request.POST['plan']
        params = {
            'plan': plan,
        }
    else:
        params = {
            'plan': '1',
        }
    return render(request, 'forum/subscribe.html', params)
