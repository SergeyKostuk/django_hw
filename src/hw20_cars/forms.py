from django import forms


class CarInfo(forms.Form):
    brand = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    color = forms.CharField(max_length=255)
    weight = forms.IntegerField(min_value=800,)
    owner_full_name = forms.CharField(max_length=255)
    release_year = forms.IntegerField()
