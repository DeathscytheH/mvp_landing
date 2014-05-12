from django import forms
from .models import signUp

class SingUpForm(forms.ModelForm):
	"""docstring for SingUpForm"""
	class Meta:
		model=signUp
