from rest_framework import serializers
from .models import Employees

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Employees
		fields = ('id', 'eid', 'ename', 'email', 'econtact')