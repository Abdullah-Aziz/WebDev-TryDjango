from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({'placeholder': 'title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'here',
            'row': 10,
            'col': 10
        }
    ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" not in title:
            raise forms.ValidationError('This is an error')
        return title

class RawProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'here',
            'row': 10,
            'col': 10
        }
    ))
    price = forms.DecimalField(initial=199.99)
