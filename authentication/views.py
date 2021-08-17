from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import Employees
from authentication.forms import EmployeeForm


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
