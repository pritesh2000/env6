from .models import User, Customer, Owner
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Field, Layout, Column


class CustomerForm(UserCreationForm):

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=10)
    profile_pic = forms.ImageField(required=False)
    address= forms.CharField(widget=forms.Textarea, required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # self.helper = FormHelper()
        # self.helper.layout = Layout(

            # Row(
            #     Field('address', wrapper_class='col-md-6', css_class='row-fluid')
            # ),

            # Column(
            #     Field('address', wrapper_class='')
            # )
        # )
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer=True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.profile_pic = self.cleaned_data.get('profile_pic')
        user.address = self.cleaned_data.get('address')
        user.save()
        customer = Customer.objects.create(user=user)
        return user

class OwnerForm(UserCreationForm):

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=10)
    profile_pic = forms.ImageField(required=False)
    address = forms.CharField(widget=forms.Textarea)

    garage_name = forms.CharField(required=True)
    garage_email = forms.EmailField(required=True)
    garage_address= forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner=True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.profile_pic = self.cleaned_data.get('profile_pic')
        user.address = self.cleaned_data.get('address')
        user.save()
        
        owner = Owner.objects.create(user=user)
        owner.garage_name = self.cleaned_data.get('garage_name')
        owner.garage_email = self.cleaned_data.get('garage_email')
        owner.garage_address = self.cleaned_data.get('garage_address')
        owner.save()
        # user.save(commit=True)
        return owner