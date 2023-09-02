from django import forms
from . models import Paystack
from projects.models import Project
import random
from django.urls import reverse


class PaymentForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    class Meta:
        model = Paystack
        fields = ('amount','email','project')


    def save(self, commit=True):
        payment = super(PaymentForm, self).save(commit=False)
        payment.project = self.cleaned_data['project']
        payment.reference = ''
        
        if commit:
            payment.save()
        return payment


    def get_verify_payment_url(self):
        # Generate the URL for verify_payment using the saved reference
        if self.instance and self.instance.reference:
            return reverse('payments:verify_payment', kwargs={'reference': self.instance.reference})
        return ""
    
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['placeholder'] = 'Amount'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'Project'
        