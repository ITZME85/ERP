from django.shortcuts import render,redirect
from .forms import*

# Create your views here.
def Quotation_form(request):
    form = quotaion_form()
    return render(request,'quotation_form.html',{'form':form})