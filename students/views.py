from django.shortcuts import render
from students.models import Student
from datetime import datetime

def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all-students.html', {'students': students})

def student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        date = int(datetime.today().strftime('%Y'))
        birthday_year = int(student.dob.strftime('%Y'))
        context = {
            'student': student,
            'age': date - birthday_year
        }
    except:
        context = {}
    return render(request, 'students/student.html', context)