from django import forms
from points.models import Points

class AddPoint(forms.Form):
    title       =forms.CharField    ()
    description =forms.CharField    (widget=forms.Textarea)

    class Meta:
        model=Points
        fields=('title','description',)
