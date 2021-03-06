from django import forms
from authentication.models import Employees, Customer, Book, Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = "__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "password"]

class CreateCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"
		exclude = ["user"]

class CreataBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = "__all__"

		