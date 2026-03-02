from django.urls import path
from .views import validate_name

urlpatterns=[
  path('validate/',validate_name),
]