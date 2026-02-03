from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test-500/', views.trigger_500),
]
