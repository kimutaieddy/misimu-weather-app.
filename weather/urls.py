# In weather/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('search/', views.search, name='search'),  # URL pattern for the search view
    # Add more URL patterns as needed for other views
]
