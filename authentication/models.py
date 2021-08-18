from django.db import models
from django.contrib.auth.models import User


class Employees(models.Model):
	eid = models.CharField(max_length=20)
	ename = models.CharField(max_length=500)
	email = models.EmailField(max_length=500)
	econtact = models.CharField(max_length=12)

	class Meta:
		db_table = "employee"

	def __str__(self):
		return f"{self.eid} : {self.ename}"


class Book(models.Model):
	title = models.CharField(max_length=200, null=True)
	Author = models.CharField(max_length=200, null=True)
	Price = models.IntegerField()
	Edition = models.IntegerField()

	def __str__(self):
		return str(self.title)

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.name)

class Cart(models.Model):
	customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
	books = models.ManyToManyField(Book)

	def __str__(self):
		return str(self.customer)