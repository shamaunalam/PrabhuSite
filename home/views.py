from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        "short_description":'This ia the under construction site coming soon'
    }
    return render(request,'index.html',context)


CompanyName = 'Bholenath Enterprises'
TagLine1 = "Your Next Dream Property"
TagLine2 = "Homes | Construction | Real Estate"

WhatWeDo = {
    "short_desc" : "___________",
    'Market_Analysis_desc':"_________",
    "Fast_Support_Desc":"___________",
    "Agents" : "_____________"
}