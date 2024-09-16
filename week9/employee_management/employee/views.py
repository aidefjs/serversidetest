from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
from .models import *
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from employee.forms import *

def formView(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูล employee โดยตรง
            return redirect("employee")
    else:
        form = EmployeeForm()

    return render(request, "employee_form.html", {"form": form})

def formprojectView(request):
    if request.method == "POST":
        form = Projectform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("project")
    else:
        form = Projectform()

    return render(request, "project_form.html", {"form": form})


class EmployeeView(View):
    def get(self, request):
        numemp = Employee.objects.count()
        info = Employee.objects.all().order_by('hire_date')
        dic = {"dicnumemp":numemp, 'info':info}
        return render(request, "employee.html", dic,)
    
class PositionView(View):
    def get(self, request):
        position = Position.objects.all().annotate(numPosi=Count('employee'))
        dic = {"position":position,}
        return  render(request, "position.html", dic,)
    
class ProjectView(View):
    def get(self, request):
        project = Project.objects.all().order_by('id')
        dic = {"project":project,}
        return  render(request, "project.html", dic,)
    
class ProjectDetailView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        projectStaff = project.staff.all()
        form = DetailForm(instance=project)
        context = {
            'form': form,
            'project': project,
            'projectStaff': projectStaff,
        }
        return render(request, 'project_detail.html', context)

    
    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = DetailForm(request.POST, instance=project)
            # save if valid                                       
        if form.is_valid():                                                                      
            form.save()                                                                          
            return redirect("detail", project_id=project.id)

        return render(request, 'project_detail.html', {'form':form})
        
    def delete(self, request, project_id, emp_id):
        try: 
            project = Project.objects.get(id=project_id)
            employee = Employee.objects.get(id=emp_id)
            project.staff.remove(employee)
            return JsonResponse({"message": "Project deleted successfully."}, status=200)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found."}, status=404)
        
    
class ProjectDeleteView(View):
    def delete(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return JsonResponse({"message": "Project deleted successfully."}, status=200)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found."}, status=404)
