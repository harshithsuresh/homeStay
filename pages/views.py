from django.shortcuts import render
from owners.models import Owner
from stays.choices import price_choices,state_choices,bedroom_choices,rating_choices
from stays.models import Stay

def index(request):
    stays=Stay.objects.order_by('-listedDate')[:3]
    context={
        "stays":stays,
        "state_choices":state_choices,
        "price_choices":price_choices,
        "bedroom_choices":bedroom_choices,
        "rating_choices":rating_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    # Get all Owners
    owners=Owner.objects.all()[:6]
    # Get Top Rating
    topRatingStayId=Stay.objects.values('avgReview','id').order_by("-avgReview").first()
    rating=topRatingStayId['avgReview']
    topRatingStayDetails=Stay.objects.filter(id=topRatingStayId['id'])[0]
    context={
        "owners":owners,
        "topRating":topRatingStayDetails,
        "rating":rating

    }
    return render(request,'pages/about.html',context)