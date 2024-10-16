from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re
from .models import Car, Driver

User = get_user_model()


class DriverCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "license_number", "email"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not re.match(r"^[A-Z]{3}\d{5}$", license_number):
            raise ValidationError(
                "License number must consist of "
                "3 uppercase letters followed by 5 digits."
            )
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not re.match(r"^[A-Z]{3}\d{5}$", license_number):
            raise ValidationError(
                "License number must consist of "
                "3 uppercase letters followed by 5 digits."
            )
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
