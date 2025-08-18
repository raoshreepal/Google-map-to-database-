from django import forms

class URLForm(forms.Form):
    maps_url = forms.URLField(label="Google Maps URL")
