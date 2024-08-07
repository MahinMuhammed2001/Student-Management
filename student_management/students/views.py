from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import StudentRegistrationForm




def register_student(request):
    if request.method=='POST':
        form= StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form= StudentRegistrationForm()
    return render(request,'register.html',{'form':form})

def student_list(request):
    students= Student.objects.all()
    return render(request,'student.html',{'students': students})


def course_list(request):
    courses= Course.objects.all()
    return render(request,'course.html',{'courses': courses})

def course_detail(request, pk):
    course= get_object_or_404(Course, pk=pk)
    students=Student.objects.filter(course=course)
    return render(request, 'course_details.html', {'course': course, 'students': students})
