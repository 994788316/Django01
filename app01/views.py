from datetime import date

from django.shortcuts import render, redirect
from app01.models import Department
# Create your views here.
def del_dep(request,dep_id):
    # d = Department.objects.get(id = dep_id)
    # d.delete()
    Department.objects.filter(id = dep_id).delete()

    return redirect('/show_deps')

def add_dep(request):
    d = Department()
    d.name = '财务部'
    d.create_date = date(2017,1,1)
    d.save()
    return redirect('/show_deps')


def show_dep(request,dep_id):
    d = Department.objects.get(id=dep_id)
    employees = d.employee_set.all()
    data = {
        'department':d,
        'employees':employees
    }
    return render(request,'show_dep.html',data)

def show_deps(request):
    deps = Department.objects.all()
    data = {
        'deps':deps
    }

    return render(request,'show_deps.html',data)





















# from django.http import HttpResponse
#
# from app01.models import Department
# def show_dep(request,dep_id):
#     d = Department.objects.get(id=dep_id)
#     employees = d.employee_set.all()
#     data = {
#         'department':d,
#         'employees':employees
#     }
#     return render(request,'show_dep.html',data)
# def show_deps(request):
#     deps = Department.objects.all()
#     data = {
#         'deps':deps,
#     }
#     return render(request,'show_deps.html',data)