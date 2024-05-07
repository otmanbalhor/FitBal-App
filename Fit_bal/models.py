from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    
    SEX_TYPES = {
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    }
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices= SEX_TYPES)
    age = models.CharField(max_length=12)
    price = models.FloatField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coachs"

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    
    SEX_TYPES = {
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    } 
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices= SEX_TYPES)
    age = models.CharField(max_length=12)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
        
class Invoice(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_datetime = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=100000, decimal_places=2)
    last_updated_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    comment = models.TextField(null=True, max_length=1000,blank=True)
    
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        
    def __str__ (self):
        return f"{self.customer.name}{self.invoice_datetime}"
    
    @property
    def get_total(self):
        subs = self.sub_set.all()
        total = sum(sub.get_total for sub in subs)
        return total
    

class Sub(models.Model):
    
    SUB_TYPES = {
        ('S','Standard'),
        ('P','Premium'),
    }
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=1, choices= SUB_TYPES)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=1000, decimal_places=2)
    total = models.DecimalField(max_digits=1000, decimal_places=2)
    
    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        
    @property
    def get_total(self):
        total = self.quantity * self.unit_price
        return total
    
class UserProfile(models.Model):

    SEX_TYPES = {
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    } 
    
    MONTH_LIST = {
        (1,'January'),
        (2,'February'),
        (3,'March'),
        (4,'April'),
        (5,'May'),
        (6,'June'),
        (7,'July'),
        (8,'August'),
        (9,'September'),
        (10,'October'),
        (11,'November'),
        (12,'December')
    }
    
    first_name= models.CharField(max_length=64)
    last_name= models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, unique=True)
    sex = models.CharField(max_length=1, choices= SEX_TYPES)
    phone = models.CharField(max_length=128)
    day = models.IntegerField()
    month = models.CharField(max_length=2, choices= MONTH_LIST)
    year = models.IntegerField()
    address = models.CharField(max_length=128)
    num_address = models.IntegerField()
    zip_code = models.CharField(max_length=16)
    city = models.CharField(max_length=32)
    
    class Meta:
        verbose_name = 'register'
        verbose_name_plural = 'registers'
    
    
    