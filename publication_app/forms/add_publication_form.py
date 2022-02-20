from django import forms


class AddPublicationForm(forms.Form):
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea, max_length=1000)
