from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentData

# Create your views here.
def AllStudent(request):
    students = StudentData.objects.all()
    return render(request,'all_students.html', {'students': students})

def AddStudent(request):
    add_form = StudentForm()
    if request.method == 'POST':
        add_form = StudentForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('all_student')
    return render(request,'add_students.html',{'add_form':add_form})

def EditStudent(request,id):
    student = StudentData.objects.get(id=id)
    edit_form = StudentForm(instance=student)
    if request.method == 'POST':
        edit_form = StudentForm(request.POST, instance=student)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_student')
    return render(request,'edit_students.html',{'edit_form':edit_form})

def DeleteStudent(request,id):
    student = StudentData.objects.get(id=id)
    student.delete()
    return redirect('all_student')