from django import forms
from .models import*

class quotaion_form(forms.ModelForm):
    class Meta:
        model = Quotaion
        fields = ['customer_name','product','date']
        # widgets = {
        #     'customer_name':forms.TextInput(
        #         attrs={
        #             'placeholder':'Name'
        #         }
        #     )
        # }
    