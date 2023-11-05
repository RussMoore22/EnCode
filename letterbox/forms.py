from django.forms import ModelForm
from .models import SecretMessage

class ComposeForm(ModelForm):
    class Meta:
        model = SecretMessage
        fields = [
            'receipient',
            'subject',
            'text',
            'encoder',

        ]
class DecipherForm(ModelForm):
    class Meta:
        model = SecretMessage
        fields = [
            'encrypted_text',
            'key',

        ]
