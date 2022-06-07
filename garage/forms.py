from .models import Category, Subcategory, Service
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    
    class Meta:
        model = Subcategory
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = '__all__'


