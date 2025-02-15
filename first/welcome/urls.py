from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Example view
    path('about/', views.about, name='about'),
]
