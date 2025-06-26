from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),  # ✅ Fixed here
    path('faq/', views.faq, name='faq'),
    path('it-solutions/', views.it_solutions, name='it_solutions'),
    path('overview/', views.overview, name='overview'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
