from django.test import TestCase
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth import get_user_model


class TestUserProfileForm(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com',
            password='testpass123'
        )
        self.profile, created = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={
                'default_phone_number': '1234567890',
                'default_country': 'US',
                'default_postcode': '12345',
                'default_town_or_city': 'Test City',
                'default_street_address1': '123 Test Street',
            }
        )

    def test_user_profile_form_valid_data(self):
        """Form is valid with correct data"""
        form = UserProfileForm(data={
            'default_phone_number': '9876543210',
            'default_country': 'US',
            'default_postcode': '54321',
            'default_town_or_city': 'New City',
            'default_street_address1': '456 New Street',
        }, instance=self.profile)
        self.assertTrue(form.is_valid())

    def test_user_profile_form_missing_required_fields(self):
        """Form should be invalid if required fields are missing"""
        form = UserProfileForm(data={})
        self.assertFalse(form.is_valid())
        required_fields = [
            'default_phone_number',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_country'
        ]
        for field in required_fields:
            self.assertIn(field, form.errors)

    def test_user_profile_form_widget_attributes(self):
        """Check that widgets have correct placeholders, classes, autofocus"""
        form = UserProfileForm(instance=self.profile)

        expected_placeholders = {
            'default_phone_number': 'Phone Number *' if form.fields[
                'default_phone_number'].required else 'Phone Number',
            'default_postcode': 'Postal Code *' if form.fields[
                'default_postcode'].required else 'Postal Code',
            'default_town_or_city': 'Town or City *' if form.fields[
                'default_town_or_city'].required else 'Town or City',
            'default_street_address1': 'Street Address 1 *' if form.fields[
                'default_street_address1'].required else 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        for field, placeholder in expected_placeholders.items():
            self.assertEqual(form.fields[field].widget.attrs['placeholder'],
                             placeholder)
            self.assertIn('border-black', form.fields[field].widget.attrs[
                'class'])
            self.assertIn('profile-form-input',
                          form.fields[field].widget.attrs['class'])

        # Check autofocus is set on the first field
        self.assertTrue(form.fields['default_phone_number'].widget.attrs[
            'autofocus'])
