from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "phone_number",
            "name",
            "purchase",
            "product",
            "extra_message",
        )
        widgets = {
            "name": forms.TextInput,
        }