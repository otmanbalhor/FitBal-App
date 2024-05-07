from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class AdminCustomer(admin.ModelAdmin):
    list_display = ('name','email','phone','address','sex','age','city','zip_code')
    
class AdminCoach(admin.ModelAdmin):
    list_display = ('name','email','phone','address','sex','age','price','city','zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer','save_by','invoice_datetime','total','last_updated_date','paid')
  


admin.site.register(Customer, AdminCustomer)
admin.site.register(Coach, AdminCoach)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Sub)
