from django.db.models.aggregates import Avg
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from .models import Stay
from django.core.paginator import Paginator
from .choices import state_choices,bedroom_choices,price_choices,rating_choices
from stays.models import Stay
from review.models import Review

from datetime import date

def stays(request):  
    stays=Stay.objects.all()
    paginator=Paginator(stays,6)
    page=request.GET.get('page')
    pageStays=paginator.get_page(page)

    context={
        "stays":pageStays
    }
 
    return render(request,'stays/stays.html',context)

def stay(request,stay_id): 
    stay=get_object_or_404(Stay,pk=stay_id)
    reviews=Review.objects.filter(stayID__exact=stay_id)
        
    context={
        'stay':stay,
        'reviews':reviews,
        'rating_choices':rating_choices,
        'today':str(date.today())
    } 
    return render(request,'stays/stay.html',context)

def review(request):
    if request.method=="POST":
        userName=request.POST['userName']
        rating=request.POST['rating']
        stayTitle=request.POST['stayTitle']
        comments=request.POST['comment']
        stayId=request.POST['stayId']

        #Checking if the user has already given review
        if Review.objects.filter(userName__iexact=userName,stayTitle__iexact=stayTitle):
            messages.warning(request,"You have already reviewed this Homestay")
            return redirect('/stays/'+stayId)

        # #Writing to review table 
        review=Review(userName=userName,rating=rating,stayTitle=stayTitle,comments=comments,stayID=stayId)
        review.save()

        # #Writing AvgReview to Stay table and reviewCount
        avgRating=Review.objects.filter(stayID__exact=stayId).aggregate(Avg('rating'))
        stayDetails=Stay.objects.get(id=stayId)
        stayDetails.avgReview=avgRating['rating__avg']
        stayDetails.countReview+=1
        stayDetails.save()

        messages.success(request,"Thanks for your review")

    return redirect('/stays/'+stayId)


def search(request):  
    queryset_list=Stay.objects.all()
    #Keywords
    if 'keywords'in request.GET:
        keywords=request.GET['keywords']
        queryset_list=queryset_list.filter(discription__icontains=keywords)
    #City
    if 'city'in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)   

    #State
    if 'state'in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)          

    #Bedrooms 
    if 'bedrooms'in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)                

    #Price
    if 'price'in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(pricePerPerson__lte=price)  
    #Rating
    if 'rating'in request.GET:
        rating=request.GET['rating']
        if rating:
            queryset_list=queryset_list.filter(avgReview__gte=rating)  

    paginator=Paginator(queryset_list,6)
    page=request.GET.get('page')
    pageStays=paginator.get_page(page)

    context={
        "state_choices":state_choices,
        "price_choices":price_choices,
        "bedroom_choices":bedroom_choices,
        "rating_choices":rating_choices,
        "stays":pageStays,
        "values":request.GET
    }   
    return render(request,'stays/search.html',context)      