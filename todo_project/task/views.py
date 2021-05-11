from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Task
from .forms import TaskForm

from django.http import JsonResponse
from django.forms.models import model_to_dict


class TaskList(View):
	def get(self, request):
		form = TaskForm()
		tasks = Task.objects.all()
		return render(request, 'task/task_list.html', {
				'form': form,
				'tasks': tasks,
			})

	def post(self, request):
		form = TaskForm(request.POST)

		if form.is_valid():
			new_task = form.save()
			return JsonResponse({'task': model_to_dict(new_task)}, status=200)
		return redirect('task_list')


class TaskComplete(View):
	def post(self, request, id):
		task = Task.objects.get(id=id)
		task.completed = True
		task.save()
		return JsonResponse({'task': model_to_dict(task)}, status=200)


class TaskDelete(View):
	def post(self, request, id):
		task = Task.objects.get(id=id)
		task.delete()
		return JsonResponse({'result': 'ok'}, status=200)
