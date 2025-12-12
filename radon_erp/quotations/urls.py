from django.urls import path
from .import views as v


urlpatterns = [
    path('',v.Quotation_form,name='home'),
]