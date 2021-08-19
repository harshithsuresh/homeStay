from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from enquires.models import  Enquire

def enquiry(request):
    if request.method=="POST":
        stayId=request.POST['stayId']
        stayTitle=request.POST['stayTitle']
        userName=request.POST['userName']
        email=request.POST['email']
        phone =request.POST['phone']
        userId=request.POST['userId']
        bookingDate=request.POST['bookingDate']
        closingDate=request.POST['closingDate']
        contact=Enquire(stayId=stayId,stayTitle=stayTitle,userName=userName,email=email,phone=phone,userId=userId,bookingDate=bookingDate,closingDate=closingDate) 
        contact.save()
    # send_mail(
    #     'Property Listing Inquery',
    #     'There is an inquery for  '+listing+ '. Sign from admin panel for more info',
    #     'harshith9921@gmail.com',
    #     [realtor_email],
    #      fail_silently=False
    # )
    messages.success(request,"You have successfully booked the room. Please check dashboard for more details")
    return redirect('/stays/'+stayId) 



