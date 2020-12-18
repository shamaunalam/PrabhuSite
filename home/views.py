from django.shortcuts import render
from .models import HomeSection
# Create your views here.
def home(request):

    Home_Page_Data = HomeSection.objects.all()


    context={
        'Companydetails': Home_Page_Data
    }
    return render(request,'index.html',context)

