from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from .models import About, FAQ, NewsletterSubscriber
from .forms import ContactForm, NewsletterForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About.objects.create(
            title="About Me",
            content="This is about me."
        )

    def test_render_about_page_with_contact_form(self):
        """Verifies GET request renders About page with contact form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactForm
        )

    def test_successful_contact_request_submission(self):
        """Test for successful contact form submission"""
        post_data = {
            'name': 'Test Name',
            'email': 'test@email.com',
            'message': 'Test message'
        }
        response = self.client.post(reverse('about'), post_data, follow=True)

        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Contact request received! "
            "I endeavour to respond within 2 working days."
        )


class TestFAQView(TestCase):

    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is CaligrifyZone?",
            answer="A calligraphy-focused art platform."
        )

    def test_faq_page_renders_successfully(self):
        """Verifies FAQ page renders correctly"""
        response = self.client.get(reverse('faq'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'What is CaligrifyZone?', response.content)
        self.assertIn(b'calligraphy', response.content.lower())


class TestNewsletterView(TestCase):

    def test_newsletter_page_renders(self):
        """Verifies newsletter subscription page renders"""
        response = self.client.get(reverse('newsletter'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['newsletter_form'], NewsletterForm
        )

    def test_successful_newsletter_subscription(self):
        """Test successful newsletter signup"""
        post_data = {
            'name': 'Radwan',
            'email': 'radwan@test.com'
        }

        response = self.client.post(
            reverse('newsletter'),
            post_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            NewsletterSubscriber.objects.filter(
                email='radwan@test.com'
            ).exists()
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Thank you for subscribing!")

    def test_duplicate_newsletter_email_not_allowed(self):
        """Prevents duplicate newsletter subscriptions"""
        NewsletterSubscriber.objects.create(
            name="Radwan",
            email="duplicate@test.com"
        )

        post_data = {
            'name': 'Another User',
            'email': 'duplicate@test.com'
        }

        response = self.client.post(
            reverse('newsletter'),
            post_data
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            NewsletterSubscriber.objects.filter(
                email='duplicate@test.com'
            ).count(),
            1
        )

        self.assertFormError(
            response,
            'newsletter_form',
            'email',
            'This email is already subscribed to our newsletter.'
        )
