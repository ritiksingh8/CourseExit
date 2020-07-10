from django.shortcuts import render,redirect
from course.models import Course,Question,Response,CourseExitStatus
from .models import Student
from django.contrib import messages
# Create your views here.


def home(request):

	if len(Student.objects.filter(user=request.user))!=0:
		sem = request.user.student.sem
		context ={
			'course':Course.objects.filter(sem=sem)
		}

		return render(request,'student/home.html',context=context)

	return render(request,'student/forbidden.html')

def redirectingview(request):

	if len(Student.objects.filter(user=request.user))!=0:
		
		return redirect('student-home')

	return redirect('teacher-home')

def show_questions(request,id):


	course_obj = Course.objects.filter(id=id).first()
	student = Student.objects.filter(user = request.user).first()
	course_exit_status_objects = CourseExitStatus.objects.filter(course=course_obj,student=student)

	if len(course_exit_status_objects)!=0:
		return render(request,'student/forbidden.html')


	questions = Question.objects.filter(course=course_obj)
	index = [(i+1) for i in range(len(questions))]
	questions_with_index = zip(index,questions)

	if request.method == 'POST':

		for index,question in questions_with_index:
			answer = str(request.POST.get(str(index),""))
			response_obj = Response(question=question,student=student,answer=answer)
			response_obj.save()

		course_exit_status_obj = CourseExitStatus(course=course_obj,student=student,status="Filled")
		course_exit_status_obj.save()
		messages.success(request,f'Your Response has been recorded!')
		return redirect('student-home')


	else:
		context = {
			'questions':questions_with_index
		}

		return render(request,'student/show_questions.html',context=context)
	


 