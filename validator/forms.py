from django import forms
import re

class NameValidationForm(forms.Form):
  name = forms.CharField(
    min_length=3,
    max_length=20,
    required=True
  )
  email = forms.EmailField(
    required=True
  )
  password = forms.CharField(
    min_length=8,
    required=True
  )

  def clean_name(self):
    name = self.cleaned_data["name"]

    if not name.isalpha():
      raise forms.ValidationError("Only letters allowed")

    if re.search(r'[aeiou]{3}', name.lower()):
      raise forms.ValidationError("Too many consecutive vowels")

    return name

  def clean_email(self):
    email = self.cleaned_data['email']

    if email.endswith("@tempmail.com"):
      raise forms.ValidationError("Temporary emails not allowed")

    return email

  def clean_password(self):
    password = self.cleaned_data['password']

    if not re.search(r"[A-Z]", password):
      raise forms.ValidationError("Password should contain an uppercase letter")

    if not re.search(r"\d", password):
      raise forms.ValidationError("Password must contain a number")

    return password

  def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")

        if not name or not password or not email:
            return cleaned_data  

        if name.lower() in password.lower():
            raise forms.ValidationError(
                "Password should not contain your name"
            )

        email_username = email.split("@")[0]
        if email_username.lower() == name.lower():
            raise forms.ValidationError(
                "Email username should not be the same as name"
            )

        return cleaned_data

