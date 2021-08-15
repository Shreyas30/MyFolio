from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from resume.models import Contact
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages 

def index(request):
    return render(request, 'index.html')

def signupUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        # Create User
        newUser = User.objects.create_user(username, email, password)
        newUser.first_name= fname
        newUser.last_name= lname
        newUser.save()
        messages.success(request, "Sign Up Successful. You can Proceed to Login Now")
        return redirect('Home')
    else:
        return HttpResponse('404 Not Found')

def loginUser(request):
    if request.method == 'POST':
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginUsername, password=loginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login Successful. We welcome you {loginUsername}")
            return redirect('Home')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('Home')
    else:
        return HttpResponse("404 Not Found")

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Home')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        field = request.POST['field']
        subscription = request.POST['subscription']
        message = request.POST['message']

        newContact = Contact()
        newContact.name = name
        newContact.email = email
        newContact.field = field
        newContact.subscription = subscription
        newContact.message = message
        newContact.save()

        if(field == 'Complaint'):
            messages.error(request,"Your Complaint is Registered Successfully. We will respond shortly")
        elif field == 'Enquiry':
            messages.info(request,"Your Enquiry is received Successfully. We will respond shortly")
        elif field == 'Feedback':
            messages.success(request,"Thank You! For your Valuable Feedback")
        return redirect('Home')
    return render(request,'contact.html')