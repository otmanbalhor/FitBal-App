from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages
from django.db import transaction

# Create your views here.

class HomeView(View):
    templates_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        
        invoices = Invoice.objects.select_related('customer','save_by').all()
        context = {
            'invoices':invoices
            }
        return render(request, self.templates_name,context)
    
    def post(self, request, *args, **kwargs):
        
        invoices = Invoice.objects.select_related('customer','save_by').all()
        context = {'invoices':invoices}
        return render(request, self.templates_name, context) 
    

class AddCoachView(View):
     
    templates_name = 'add_coach.html'
     
    def get(self, request, *args, **kwargs):
        
        return render(request, self.templates_name)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone':request.POST.get('phone'),
            'sex':request.POST.get('sex'),
            'age':request.POST.get('age'),
            'price':request.POST.get('price'),
            'address':request.POST.get('address'),
            'city':request.POST.get('city'),
            'zip_code':request.POST.get('zip_code'),
            'save_by':request.user
        }
        
        try:
            created = Coach.objects.create(**data)
            
            if created:
                messages.success(request, 'Coach registered successfully.')
                
            else:
                messages.error(request, "Error, please try again.")
        
        except Exception as e:
            messages.error(request,f"sorry our system is detecting the following issues : {e}.")
        
        return render(request, self.templates_name)
    
    

class AddCustomerView(View):
     
    templates_name = 'add_customer.html'
     
    def get(self, request, *args, **kwargs):
        
        return render(request, self.templates_name)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone':request.POST.get('phone'),
            'sex':request.POST.get('sex'),
            'age':request.POST.get('age'),
            'address':request.POST.get('address'),
            'city':request.POST.get('city'),
            'zip_code':request.POST.get('zip_code'),
            'save_by':request.user
        }
        
        try:
            created = Customer.objects.create(**data)
            
            if created:
                messages.success(request, 'Customer registered successfully.')
                
            else:
                messages.error(request, "Error, please try again.")
        
        except Exception as e:
            messages.error(request,f"sorry our system is detecting the following issues : {e}.")
        
        return render(request, self.templates_name)
    
    
class AddInvoiceView(View):
     
    templates_name = 'add_invoice.html'
     
    
    def get(self, request, *args, **kwargs):
        
        customers = Customer.objects.select_related('save_by').all()
        context = {
            'customers':customers
            }
        return render(request, self.templates_name,context)
    
    
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        
        
        try:
            
            customer_id = request.POST.get('customer')
            
            subTypes = request.POST.get('sub')
            
            quantities = request.POST.get('quantity')
            
            units = request.POST.get('unit')
            
            totalSubs = request.POST.get('total-sub')
            
            total = request.POST.get('total')
            
            comment = request.POST.get('comment')
            
            invoice = Invoice.objects.create(
                customer_id=customer_id,
                save_by=request.user,
                total=total,
                comment=comment
            )
            
            items = []
            
            for subType, quantity, unit, totalSub in zip(subTypes, quantities, units, totalSubs):
                item = Sub(
                    invoice=invoice,
                    name=subType,
                    quantity=quantity,
                    unit_price=unit,
                    total=totalSub
                )
                
                items.append(item)
                
            created = Sub.objects.bulk_create(items)
            
            if created:
                messages.success(request, 'Data saved successfully.')
                
            else:
                messages.error(request, "Error, please try again.")
        
        except Exception as e:
            messages.error(request,f"sorry our system is detecting the following issues : {e}.")
        
        return render(request, self.templates_name)