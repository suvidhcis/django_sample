from django.contrib import admin
from authentication.models import Employees, Customer, Book, Cart

# Register your models here.
admin.site.register(Employees)
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Cart)
