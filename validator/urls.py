from django.urls import path
from .views import validate_name, success

urlpatterns=[
  path("", validate_name,name = "validation"),
  path("success/", success, name ="success"),
]