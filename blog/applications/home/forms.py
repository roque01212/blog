from django import forms

#
from .models import Contact, Suscribers


class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        """Meta definition for Suscribersform."""

        model = Suscribers
        fields = ('email',)
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Correo Electronico...',
                    
                }
            )
        }


class ContacForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('__all__')