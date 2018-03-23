from django.contrib import admin
from app01.models import Department,Employee
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name','create_date']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age','sex','salary','comment']

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)

























# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ['id','name','create_date']
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['id','name','age','sex','salary','comment']
#
#
# admin.site.register(Department,DepartmentAdmin)
#
# admin.site.register(Employee,EmployeeAdmin)


















