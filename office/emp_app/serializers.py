from rest_framework import serializers
from .models import Employee, Department, Role

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    dept = DepartmentSerializer()
    role = RoleSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
