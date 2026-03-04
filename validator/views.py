from django.shortcuts import render, redirect
from .forms import NameValidationForm

def validate_name(request):
  if request.method == "POST":
    form = NameValidationForm(request.POST)

    if form.is_valid():
      return redirect("success") 
  else:
    form = NameValidationForm()

  return render(request,"validator/form.html",{
    "form":form
  }
)

def success(request):
  return render(request, "validator/success.html")