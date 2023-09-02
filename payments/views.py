from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from  .models import Paystack
from .forms import PaymentForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Userhistory


@login_required(login_url='/login')
def InitializeDeposit(request):
    value = {
        'email': request.user.email
    }
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment=payment_form.save()
            verify_payment_url = payment_form.get_verify_payment_url()
            return render(request, 'confirm.html', {'payment':payment,'verify_payment_url': verify_payment_url,'PUBLIC_KEY':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form =  PaymentForm(initial=value)
    args = {'forms':payment_form}
    return render(request, 'make_payment.html', args)

@login_required(login_url='/login')
def verify_payment(request, reference):
    payment = get_object_or_404(Paystack, reference=reference)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Successful Deposit')
    else:
        messages.error(request, 'Incomplete Deposit Transaction')
    return redirect('/')
    
               
# @login_required(login_url='/login')
# def make_payment(request):
#     return render(request, 'make_payment.html', {})
    
    

