from django.forms import ModelForm
from .models import Review, Modification

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['rating', 'comment']

class ModificationForm(ModelForm):
  class Meta:
    model = Modification
    fields = ['content']