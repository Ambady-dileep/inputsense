from django import forms
import re

class NameValidationForm(forms.Form):
  name = forms.CharField(
    min_length=3,
    max_length=20,
    required=True
  )

  def clean_name(self):
    name = self.cleaned_data["name"]

    if not name.isalpha():
      raise forms.ValidationError("Only letters allowed")
    
    if re.search(r'[aeiou]{3}', name.lower()):
      raise forms.ValidationError("Too many consecutive vowels")

    return name 