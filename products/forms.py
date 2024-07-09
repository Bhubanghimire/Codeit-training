from django import forms
from products.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # exclude = ['name']

    # def clean_name(self):
    #     print("clean name", self.cleaned_data['name'])
    #     return self.cleaned_data
