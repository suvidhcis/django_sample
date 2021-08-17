from django.urls import path

from . import views

app_name = "authentication"

urlpatterns = [
    path('', views.index, name='index'),
    path('emp/', views.employee, name='employee'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]