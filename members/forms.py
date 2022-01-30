from django import forms
from .models import MemberProfile


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Rename fields to user friendly display on form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone No.',
            'default_street_address1': 'Address 1',
            'default_street_address2': 'Address 2',
            'default_town_or_city': 'Town / City',
            'default_county': 'County',
            'default_postcode': 'Post Code',
            'default_country': 'Country',
        }

        # Add asterisk to any fields set as required /mandatory
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set fields to user friendly names defined above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Applies class to all input fields
            self.fields[field].widget.attrs['class'] = 'profile-style-input'
            # Remove default fields labels as placeholders will be used
            self.fields[field].label = False
