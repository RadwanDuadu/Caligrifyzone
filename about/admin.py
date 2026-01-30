from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Contact, FAQ, NewsletterSubscriber


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')


@admin.register(FAQ)
class FAQAdmin(SummernoteModelAdmin):
    summernote_fields = ('answer',)
    list_display = ('question', 'order')


@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on', 'active')
    list_filter = ('active', 'subscribed_on')
    search_fields = ('email',)
