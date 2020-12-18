from django.db import models

# Create your models here.

class HomeSection(models.Model):
    
    CompanyName = models.CharField(max_length=50)
    TagLine1 = models.CharField(max_length=50)
    TagLine2 = models.CharField(max_length=50)

    def __str__(self):
        return self.CompanyName

class WhatWeDo(models.Model):
    short_desc = models.CharField(max_length=500)
    
    Market_Analysis_desc = models.CharField(max_length=500)
    
    Fast_Support_Desc = models.CharField(max_length=500)
    
    Agents = models.CharField(max_length=500)
    def __str__(self):
        return self.short_desc