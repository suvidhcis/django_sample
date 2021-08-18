from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "authentication"

routers = routers.DefaultRouter()
routers.register(r"employees", views.EmployeeViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('emp/', views.employee, name='employee'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    #DRF urls
    path('api/', include(routers.urls)),
    #Bookstore Urls
    path('home/', views.home, name='home'),
    path("login/", views.login, name="login"),
    path("viewcart/", views.viewcart, name="viewcart"),
    path("addbook/", views.addbook, name="addbook"),
    path("register/", views.register, name="register"),
    path("logout/", views.logoutPage, name="logoutPage"),
    path("addtocart/<str:pk>", views.addtocart, name="addtocart")
]