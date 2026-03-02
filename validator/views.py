from django.http import JsonResponse
from .forms import NameValidationForm

def validate_name(request):
  form = NameValidationForm(request.GET)

  if form.is_valid():
    return JsonResponse({
      "status": "valid",
      "clean_name": form.cleaned_data["name"]
    })

  return JsonResponse({
    "status":"invalid",
    "errors":form.errors
  }, status=400)