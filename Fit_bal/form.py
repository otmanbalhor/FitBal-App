from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'autocomplete': 'Name and Lastname', 'class':'form-control'}),
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'autocomplete': 'email', 'class':'form-control'}),
    )
    
    sex = forms.ChoiceField(
        label = "Sex", 
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    password1 = forms.CharField(
        label = "Password",
        strip= False, 
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),
    )
   
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),
        strip=False,
    )
    
    phone = forms.IntegerField(
        label = "Phone",
        widget=forms.TextInput(attrs={'autocomplete': 'phone','class':'form-control'})
    )
    
    day = forms.IntegerField(
        label = "Day",
        widget=forms.TextInput(attrs={'autocomplete': 'day','class':'form-control'})
    )
    
    month = forms.CharField(
        label = "Month",
        widget=forms.TextInput(attrs={'autocomplete': 'month','class':'form-control'})
    )
    
    year = forms.IntegerField(
        label = "Year",
        widget=forms.TextInput(attrs={'autocomplete': 'year','class':'form-control'})
    )
    
    address = forms.CharField(
        label = "Address",
        widget=forms.TextInput(attrs={'autocomplete': 'address','class':'form-control'})
    )
    
    numero = forms.IntegerField(
        label = "Numero",
        widget=forms.TextInput(attrs={'autocomplete': 'numero','class':'form-control'})
    )
    
    zip_code = forms.CharField(
        label = "Zip Code",
        widget=forms.TextInput(attrs={'autocomplete': 'zip','class':'form-control'})
    )
    
    city = forms.CharField(
        label = "City",
        widget=forms.TextInput(attrs={'autocomplete': 'city','class':'form-control'})
    )
    
    class Meta(UserCreationForm.Meta):
        fields =  ("name","email","sex","password1", "password2","phone","day","month","year","address","numero","zip_code","city")
        

