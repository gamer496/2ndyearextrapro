from django import forms
from places.models import Places

class AddPlace(forms.Form):
    company     =forms.CharField    ()
    country     =forms.CharField    ()
    state       =forms.CharField    ()
    city        =forms.CharField    ()
    address     =forms.CharField    ()

    class Meta:
        model=Places
        exclude=('wuser','wusersupvoted','wusersdownvoted',)
