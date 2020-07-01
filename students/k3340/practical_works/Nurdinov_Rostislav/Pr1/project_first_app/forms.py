from django import forms
from .models import Owner, Auto


# creating a form
class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "date_of_birth"
        ]
