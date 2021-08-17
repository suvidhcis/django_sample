from django.db import models


class Employees(models.Model):
	eid = models.CharField(max_length=20)
	ename = models.CharField(max_length=500)
	email = models.EmailField(max_length=500)
	econtact = models.CharField(max_length=12)

	class Meta:
		db_table = "employee"

	def __str__(self):
		return f"{self.eid} : {self.ename}"
