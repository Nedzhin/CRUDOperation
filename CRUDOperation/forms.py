from django import forms
from CRUDOperation.models import DiseaseType

class DiseaseTypeforms(forms.ModelForm):
  class Meta:
    model = DiseaseType
    fields = "__all__"
