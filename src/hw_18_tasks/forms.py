from django import forms


class FIOFORMS(forms.Form):
    firstname = forms.CharField(max_length=20,)
    sname = forms.CharField(max_length=20)

    age = forms.IntegerField(min_value=0, max_value=99,)



