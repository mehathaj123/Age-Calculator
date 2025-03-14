from django.urls import path
from .views import index  # Import the index view function

urlpatterns = [
    path('', index, name='index'),  # Route for homepage
]
