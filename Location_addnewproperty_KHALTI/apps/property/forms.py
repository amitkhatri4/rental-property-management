from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()


from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'slug', 'category', 'price', 'description', 'latitude','longitude', 'image']