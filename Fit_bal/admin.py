from django.contrib import admin
from .models import *


class AdminCustomer(admin.ModelAdmin):
    list_display = ('name','email','phone','address','sex','age','city','zip_code')
    
class AdminCoach(admin.ModelAdmin):
    list_display = ('name','email','phone','address','sex','age','price','city','zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer','save_by','invoice_datetime','total','last_updated_date','paid')
    
#class AdminSub(admin.ModelAdmin):
 #   list_display = ('invoice','name','quantity','unit_price','total')
    
admin.site.register(Customer, AdminCustomer)
admin.site.register(Coach, AdminCoach)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Sub)