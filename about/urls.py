from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('faq/', views.faq_page, name='faq'),
    path('newsletter/', views.subscribe_newsletter, name='newsletter'),
]
