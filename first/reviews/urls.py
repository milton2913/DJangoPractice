from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='reviews_index'),  # Example view
    path('details/', views.details, name='details'),
]
