from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'payments'

urlpatterns = [
    path('paystack/', InitializeDeposit, name='paystack_deposit'),
    path('<str:reference>/', verify_payment, name='verify_payment'),   
    # path('make_payment',make_payment, name="make_payment"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)