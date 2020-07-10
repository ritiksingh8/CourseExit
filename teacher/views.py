from django.shortcuts import render
from .models import FacultyCourseMapping,Teacher
from course.models import Question, Course
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def home(request):

	if len(Teacher.objects.filter(user=request.user))!=0:
		context ={
			'faculty_course_mappings': FacultyCourseMapping.objects.filter(teacher = request.user.teacher)
		}

		return render(request,'teacher/home.html',context=context)

	return render(request,'student/forbidden.html')


def show_questions(request,id):
	if len(Teacher.objects.filter(user=request.user))!=0:

		course_obj = Course.objects.filter(id=id).first()

		Questions = Question.objects.filter(course=course_obj)

		context = {'questions':Questions}

		return render(request,'teacher/show_questions.html',context)

	return render(request,'student/forbidden.html')	

class QuestionCreateView(LoginRequiredMixin, CreateView):
	model=Question	
	fields=['question']

	def form_valid(self,form):
		course_obj = Course.objects.filter(id=self.kwargs['id']).first()
		form.instance.course = course_obj
		return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model=Question	
	fields=['question']

	def form_valid(self,form):
		course_obj = Course.objects.filter(id=self.kwargs['id']).first()
		form.instance.course = course_obj
		return super().form_valid(form)

	def test_func(self):

		course_obj = Course.objects.filter(id=self.kwargs['id']).first()
		faculty_course_mappings = FacultyCourseMapping.objects.filter(course = course_obj)

		for faculty_course_mapping in faculty_course_mappings:
			if self.request.user == faculty_course_mapping.teacher.user:
				return True

		return False	

class QuestionDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model=Question
	success_url=''

	def test_func(self):

		self.success_url = '/teacher/course/{}/questions'.format(self.kwargs['id'])

		course_obj = Course.objects.filter(id=self.kwargs['id']).first()
		faculty_course_mappings = FacultyCourseMapping.objects.filter(course = course_obj)

		for faculty_course_mapping in faculty_course_mappings:
			if self.request.user == faculty_course_mapping.teacher.user:
				return True

		return False			




