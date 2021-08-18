from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import Employees, Customer, Book, Cart
from authentication.forms import EmployeeForm, CreateUserForm, CreateCustomerForm, CreataBookForm
from rest_framework import viewsets
from .serializers import EmployeeSerializer

#django CRUD operations
def index(request):
	return HttpResponse("<h1>This is the Django Crud app.</h2>")

def employee(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/show")
	else:
		form = EmployeeForm()
	context = {"form": form}
	return render(request, "authentication/index.html", context)

def show(request):
	employee = Employees.objects.all()
	return render(request, "authentication/show.html", {"employees": employee})

def edit(request, id):
	employee = Employees.objects.get(id=id)
	return render(request, "authentication/edit.html", {"employees": employee})

def update(request, id):
	employee = Employees.objects.get(id=id)
	form = EmployeeForm(request.POST, instance = employee)
	if form.is_valid():
		form.save()
		return redirect("/show")
	return render(request, 'authentication/edit.html', {"employees": employee, "form": form})

def delete(request, id):
	employee = Employees.objects.get(id=id)
	employee.delete()
	return redirect("/show")

#Django Rest Framework Api's
class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employees.objects.all().order_by('ename')
	serializer_class = EmployeeSerializer

#Django BookStore
def home(request):
	books = Book.objects.all()
	context = {"books": books}
	if request.user.is_staff:
		return render(request, 'book/adminhome.html', context)
	else:
		return render(request, 'book/home.html', context)

def logoutPage(request):
	logout(request)
	return redirect('/home')

def login(request):
	if request.user.is_authenticated:
		return redirect("/home")
	else:
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")

