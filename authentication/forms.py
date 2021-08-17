from django import forms
from authentication.models import Employees

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = "__all__"
		