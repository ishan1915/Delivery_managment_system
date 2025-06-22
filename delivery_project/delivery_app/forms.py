from django import forms
from .models import User, Customer, Order,WarehouseManager

class CustomerSignUpForm(forms.ModelForm):
    address = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField()
    pincode = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'customer'
        if commit:
            user.save()
            Customer.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone=self.cleaned_data['phone'],
                city=self.cleaned_data['city'],
                pincode=self.cleaned_data['pincode']
            )
        return user

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'description','price']


 

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'address', 'phone', 'city', 'pincode']
        widgets = { 
            'address': forms.Textarea(attrs={'rows': 2}),
            'phone': forms.TextInput(attrs={'placeholder': '10-digit phone'}),
            'city': forms.TextInput(),
            'pincode': forms.TextInput(),
        }



class WarehouseManagerProfileForm(forms.ModelForm):
    class Meta:
        model = WarehouseManager
        fields = [ 'location', 'phone', 'warehouse_name', 'pincode']
        widgets = { 
            'location': forms.Textarea(attrs={'rows': 2}),
            'phone': forms.TextInput(attrs={'placeholder': '10-digit phone'}),
            'warehouse_name': forms.TextInput(),
            'pincode': forms.TextInput(),
        }
