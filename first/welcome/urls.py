from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.welcome_home, name='welcome_home'),  # Example view
    path('about/', views.about, name='about'),
]
