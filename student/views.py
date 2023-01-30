from django.shortcuts import render, redirect
from student.models import Student
from django.contrib import messages
from .forms import StudentForm


# Create your views here.

def index(request):
    return render(request, 'student/index.html')


# Long method

# def student_page(request):
#     form = StudentForm()

#     if request.method == 'POST':
#         form = StudentForm(request.POST)

#         if form.is_valid():
#             # Get student data from inside the student form
#             student_data = {
#                 'first_name': form.cleaned_data.get('first_name'),
#                 'last_name': form.cleaned_data.get('last_name'),
#                 'number': form.cleaned_data.get('number'),
#                 'profile_pic': form.cleaned_data.get('profile_pic'),
#             }
#             # Save data to database
#             student = Student(**student_data)

#             if 'profile_pic' in request.FILES:
#                 student.profile_pic = request.FILES['profile_pic']
#             student.save()
#             return redirect('index')

#     context = {
#         'form': form
#     }
#     return render(request, 'student/student.html', context)


# Short method

def student_page(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()

        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            student.save()
        messages.success(request, "Student added successfully")
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)