from django import forms
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class MessageForm(forms.ModelForm):
    contenido = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':4})
    )

    class Meta:
        model  = Message
        fields = ['contenido']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)   
        super().__init__(*args, **kwargs)
        if user:
            self.fields['receptor'].queryset = (
                User.objects
                    .filter(is_active=True)
                    .exclude(pk=user.pk)
            )

class ReplyForm(forms.ModelForm):
    contenido = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 2,
            'placeholder': 'Escribe tu mensaje...'
        })
    )

    class Meta:
        model = Message
        fields = ['contenido']