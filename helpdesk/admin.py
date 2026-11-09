from django.contrib import admin
from .models import Department , Employee , SupportTicket

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    search_fields = ['name', 'code']



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_code', 'name', 'email', 'department',]
    search_fields = ['name', 'employee_code', 'email']
    list_filter = ['department']


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = [
        'id' , 'subject', 'employee', 
        'category', 'priority', 'status', 'assigned_to'
    ]
    search_fields = ['subject' , 'employee_name']
    list_filter = ['category' , 'priority', 'status']

