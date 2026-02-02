from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Make these fields required
        required_fields = [
            'default_phone_number',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_country'
        ]
        for field in required_fields:
            self.fields[field].required = True

        # Set placeholders, classes, labels, autofocus
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            if field_name != 'default_country':
                placeholder = placeholders.get(field_name, '')
                if field.required:
                    placeholder += ' *'
                field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')
            field.label = False
