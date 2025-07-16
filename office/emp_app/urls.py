from django.urls import path
from . import views
from .api_views import EmployeeListCreateAPI, EmployeeRetrieveUpdateDeleteAPI

urlpatterns = [
    # Old template-based views
    path('', views.index, name='home'),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),

    # New REST API endpoints
    path('api/employees/', EmployeeListCreateAPI.as_view(), name='api_all_emps'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDeleteAPI.as_view(), name='api_single_emp'),
]
