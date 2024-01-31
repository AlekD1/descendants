from django import forms

from home.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'name',
                    'placeholder': 'ФИО'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'name': 'email',
                    'placeholder': 'E-mail'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'type': 'tel',
                    'name': 'phone',
                    'placeholder': 'Телефон'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'type': 'tel',
                    'name': 'message',
                    'placeholder': 'Сообщение',
                    'id': '',
                    'cols': '',
                    'rows': '6'
                }
            )
        }