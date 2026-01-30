from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, FAQ, NewsletterSubscriber
from .forms import ContactForm, NewsletterForm


# About page view
def about_me(request):
    """Handles About page and Contact form submissions"""
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                "Contact request received! I endeavour to respond within 2 working days."
            )
            return redirect('about')  # Prevents double submission
    else:
        contact_form = ContactForm()

    about = About.objects.order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )


# FAQ page view
def faq_page(request):
    """Renders FAQ page with all questions in order"""
    faqs = FAQ.objects.all()
    return render(
        request,
        "about/faq.html",
        {"faqs": faqs}
    )


# Newsletter subscription view
def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            return redirect('newsletter')  # or any page
    else:
        form = NewsletterForm()

    return render(request, 'about/newsletter.html', {'newsletter_form': form})
