from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

from .models import *

def pagination(request, invoices):
    default_page = 1
        
    page = request.GET.get('page',default_page)
        
    perPage = 5
        
    paginator = Paginator(invoices, perPage)
        
    try:
            
        items_page = paginator.page(page)
            
    except PageNotAnInteger:
            
        items_page = paginator.page(default_page)
        
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)
            
    return items_page

def get_invoice(pk):
    
        
    obj = Invoice.objects.get(pk=pk)
        
    subs = obj.sub_set.all()
        
    context = {
            'obj':obj,
            'subs':subs
        }
    
    return context