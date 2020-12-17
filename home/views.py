from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        "short_description":'This ia the under construction site coming soon'
    }
    return render(request,'index.html',context)