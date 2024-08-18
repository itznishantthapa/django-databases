from django.shortcuts import render, redirect
from .models import MyAppDB
# Create your views here.

def home_page(request):
    data=MyAppDB.objects.first()
    return render(request,'index.html',{'data':data})

# Ways of getting data from the database;

     # first()
# obj = YourModelName.objects.filter(age__gt=18).first()


     # all()
# objects = YourModelName.objects.all()


      # get()
# obj = YourModelName.objects.get(name='Nishant')


    # filter()----------------------------------
# MyAppDB.objects.filter(age__gt=18)
# __lt: Less than
# __lte: Less than or equal to
# __gte: Greater than or equal to
# __exact: Exactly equal to
# __contains: Contains (for text fields)

