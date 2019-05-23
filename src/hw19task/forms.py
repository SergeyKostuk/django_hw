from django import forms


class AvioSaleForms(forms.Form):
    firstname = forms.CharField(max_length=20,)
    from_ = forms.CharField(max_length=20)
    arrival_ = forms.CharField(max_length=20,)
    number_of_tickets = forms.IntegerField(min_value=0, max_value=99,)
    date_ = forms.DateField()


