from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('services.html', views.services, name='services'),
    path('about-us.html', views.about, name='about'),
    path('team.html', views.team, name='team'),
    path('class-details.html', views.class_details, name='class-details'),
    path('blog.html', views.blog, name='blog'),
    path('gallery.html', views.gallery, name='gallery'),

    # Additional paths can be added here
]