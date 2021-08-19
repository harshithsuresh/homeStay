from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from enquires.models import Enquire
from stays.choices import rating_choices


def register(request):
    if request.method=='POST':
        #Get Values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #Check Values
        if password2==password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,"Now you are registered and can login")
                    return redirect('login')
        else:    
            messages.error(request,'Password does not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,"You are logged out now")
        return redirect('index')

def dashboard(request):
    enquires=Enquire.objects.filter(userId__exact=request.user.id)
    context={
        'enquires':enquires,
        'rating_choices':rating_choices
    }
    return render(request,'accounts/dashboard.html',context)

def cancelBooking(request,bookingID):
    Enquire.objects.filter(id__exact=bookingID).delete()
    messages.success(request,"Booking canceled successfully")
    return redirect('dashboard')   
