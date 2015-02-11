from django import forms
from .models import Bunk
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

class BunkSomeoneForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request", None)
		super(BunkSomeoneForm, self).__init__(*args, **kwargs)
		self.fields["to_user"].queryset = User.objects.all().exclude(username=self.request.user.username)

	to_user = forms.ModelChoiceField(queryset=None, empty_label="", label="Bunk User")
	class Meta:
		model = Bunk
		fields = ('to_user',)