from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from .form import CustomUserCreationForm
import pdfkit 
from django.template.loader import get_template
from django.db import transaction
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


from .decorators import *

from .utils import pagination, get_invoice

# Create your views here.

class HomeView(LoginRequiredSuperuserMixin,View):
    templates_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        
        invoices = Invoice.objects.select_related('customer','save_by').all().order_by('-invoice_datetime')
        context = {
            'invoices':invoices
            }
        
        items = pagination(request,invoices)
        context['invoices'] = items
        
        return render(request, self.templates_name,context)
    

    def post(self, request, *args, **kwargs):
        
        invoices = Invoice.objects.select_related('customer','save_by').all()
        context = {'invoices':invoices}
        
        if request.POST.get('id_modified'):
            
            paid = request.POST.get('modified')
            
            try:
                item = Invoice.objects.get(id=request.POST.get('id_modified'))
                if paid == 'True':
                    item.paid = True
                else:
                    item.paid = False
                item.save()
                messages.success(request, 'Change made successfully')
            except Exception as e:
                messages.error(request, f"Sorry, the following error has occured : {e}")
        
        
        if request.POST.get('id_supprimer'):
            
            try:
                item = Invoice.objects.get(id=request.POST.get('id_supprimer'))
                
                item.delete()
                
                messages.success(request, 'The invoice has been deleted successfully.')
                
            except Exception as e:
                messages.error(request, f"Sorry, the following error has occured : {e} ")
        
        items = pagination(request,invoices)
        context['invoices'] = items
        return render(request, self.templates_name, context) 
    

class AddCoachView(LoginRequiredSuperuserMixin,View):
     
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
    
    

class AddCustomerView( LoginRequiredSuperuserMixin, View):
     
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
    
    
class AddInvoiceView(LoginRequiredSuperuserMixin,View):
     
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
            
            quantities = request.POST.getlist('quantity')
            
            units = request.POST.getlist('unit')
            
            totalSubs = request.POST.getlist('total-sub')
            
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
    

class InvoiceVisualizationView(LoginRequiredSuperuserMixin,View):
    
    template_name = 'invoice.html'
    
    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')
        
        context = get_invoice(pk)
        
        return render(request, self.template_name, context)
    
@superuser_required   
def get_invoice_pdf(request, *args, **kwargs):
    
    pk = kwargs.get('pk')
    
    context = get_invoice(pk)
    
    context['date'] = datetime.datetime.today()
    
    template = get_template('invoice_pdf.html')
    
    html = template.render(context)
    
    # option of pdf format
    
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access':"",
    }
    
    # generate pdf
    
    pdf = pdfkit.from_string(html, False, options)
    
    response = HttpResponse(pdf, content_type='application/pdf')
   
    response['Content-Disposition'] = "attachement"
    
    return response
    
    
    
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html',{'form':form})