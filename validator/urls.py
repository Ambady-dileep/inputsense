from django.urls import path
from .views import validate_details, success

urlpatterns=[
  path("", validate_details,name = "validation"),
  path("success/", success, name ="success"),
]