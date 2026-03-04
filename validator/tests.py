from django.test import TestCase
from .forms import NameValidationForm

class NameValidationFormTest(TestCase):

  def test_valid_data(self):
    form = NameValidationForm(data={
      "name":"Ambady",
      "email": "test@gmail.com",
      "password": "Secure123"
    })

    self.assertTrue(form.is_valid())