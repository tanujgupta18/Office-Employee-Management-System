from django.shortcuts import render,HttpResponse
from .models import Emp,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'home.html')

def all_emp(request):
    emp = Emp.objects.all()
    context = {
        'emps':emp
    }
    return render(request,'view_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        salary = request.POST['salary']
        dept = request.POST['dept']
        role = request.POST['role']
        bonus = request.POST['bonus']
        phone = request.POST['phone']

        new_emp = Emp(fname=fname, lname=lname, salary=salary, dept_id=dept, role_id=role, phone=phone, bonus=bonus, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Successfully Added")
    elif request.method == "GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Error Occured!")

def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Emp.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter a valid EMP ID")
    emps = Emp.objects.all()
    context = {
        'emps':emps 
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Emp.objects.all()
        if name:
            emps = emps.filter(Q(fname__icontains = name) | Q(lname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        
        context = {
            'emps': emps
        }
        return render(request,'view_emp.html',context)  
    
    elif request.method == "GET":
        return render(request,'filter_emp.html')
    
    else:
        return HttpResponse("An Exception Occcured")