from datetime import datetime
from django.db import models
from owners.models import Owner
from multiselectfield import MultiSelectField

hostWelcomeChoices = (
    ("Families", "Families"),
    ("Couples", "Couples"),
    ("Students", "Students"),
    ("Males", "Males"),
    ("Females", "Females"),    
)
amenities= (
    ("Free parking", "Free parking"),
    ("Children Activities", "Children Activities"),
    ("Free Internet", "Free Internet"),
    ("Dry cleaning", "Dry cleaning"),
    ("TV", "TV"),    
)
meals=(
    ('Provided','Provided'),
    ('Use Kitchen','Use Kitchen')
)

class Stay(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.DO_NOTHING)
    title =models.CharField(max_length=200)
    city =models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    zipcode =models.CharField(max_length=20)
    discription =models.TextField(blank=True)
    maxNoPerson =models.IntegerField()
    bedrooms =models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    photoMain=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    photo2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    photo3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    photo4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    photo5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    photo6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)    
    listedDate=models.DateField(default=datetime.now,blank=True)
    pricePerPerson=models.IntegerField()
    hostWelcome=MultiSelectField(choices=hostWelcomeChoices)
    amenities=MultiSelectField(choices=amenities)
    meals=MultiSelectField(choices=meals)
    avgReview=models.DecimalField(blank=True,max_digits=2,decimal_places=1)
    countReview=models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.title