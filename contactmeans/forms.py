from django import forms
from contactmeans.models import Messages

class MessageForm(forms.Form):
    message     =forms.CharField    (widget=forms.Textarea)

    class Meta:
        model=Messages
        fields=('message',)
