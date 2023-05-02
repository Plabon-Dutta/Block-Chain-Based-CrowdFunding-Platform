from django import forms
from .models import Blog

class TextForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea, required = True)

class DonationForm(forms.Form):
    amount = forms.FloatField()

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "amount",
            "category",
            "banner",
            "description"
        )