from django.urls import path
from .views import validate_details, success, reset

urlpatterns=[
  path("", validate_details,name = "validation"),
  path("success/", success, name ="success"),
  path("reset/", reset, name="reset"),
]