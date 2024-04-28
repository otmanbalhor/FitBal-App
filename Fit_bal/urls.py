from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('add-customer',views.AddCustomerView.as_view(), name='add-customer'),
    path('add-coach',views.AddCoachView.as_view(), name='add-coach'),
    path('add-invoice',views.AddInvoiceView.as_view(), name='add-invoice'),
    
]
