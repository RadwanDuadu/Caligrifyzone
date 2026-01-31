from django.test import TestCase
from .forms import ContactForm, NewsletterForm
from .models import NewsletterSubscriber


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = ContactForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Contact Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = ContactForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ContactForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ContactForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )


class TestNewsletterForm(TestCase):

    def test_newsletter_form_is_valid(self):
        """Test valid newsletter form"""
        form = NewsletterForm({
            'name': 'Radwan',
            'email': 'radwan@test.com'
        })
        self.assertTrue(
            form.is_valid(),
            msg="Newsletter form is not valid"
        )

    def test_name_is_required(self):
        """Test name field is required"""
        form = NewsletterForm({
            'name': '',
            'email': 'test@test.com'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test email field is required"""
        form = NewsletterForm({
            'name': 'Radwan',
            'email': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_duplicate_email_not_allowed(self):
        """Test duplicate email validation"""
        NewsletterSubscriber.objects.create(
            name='Existing User',
            email='duplicate@test.com'
        )

        form = NewsletterForm({
            'name': 'New User',
            'email': 'duplicate@test.com'
        })

        self.assertFalse(
            form.is_valid(),
            msg="Duplicate email was accepted"
        )

        self.assertIn(
            'email',
            form.errors
        )
