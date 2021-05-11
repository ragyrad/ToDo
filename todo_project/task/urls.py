from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('<str:id>/completed/', views.TaskComplete.as_view(), name='task_complete'),
    path('<str:id>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]
