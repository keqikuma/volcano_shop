from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'image',
            'category',
            'brand',
            'condition',
            'tags',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'tags': forms.TextInput(attrs={'placeholder': '例如：二手，书籍，生活'}),
            'category': forms.TextInput(attrs={'placeholder': '如：电子、图书、家居'}),
            'condition': forms.Select(),
        }
