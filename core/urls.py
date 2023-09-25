# Importando a função 'path' do módulo 'django.urls'
from django.urls import path

# Importando as classes de visualização relacionadas aos estudantes e tarefas
from studyControl.views.studentTaskView import StudentTasksView
from studyControl.views.studentView import StudentListCreateView, StudentDetailView
from studyControl.views.subjectView import SubjectListCreateView, SubjectDetailView
from studyControl.views.taskView import TaskListCreateView, TaskDetailView

# Lista de URLs e suas associações com as classes de visualização

# URL para listar e criar estudantes
urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    # URL para visualizar detalhes de um estudante com base no 'pk' (chave primária)
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    # URL para listar tarefas de um estudante com base no 'aluno_id'
    path('students/<int:aluno_id>/tasks/', StudentTasksView.as_view(), name='student-tasks'),
    
    # URL para listar e criar disciplinas
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    # URL para visualizar detalhes de uma disciplina com base no 'pk'
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    
    # URL para listar e criar tarefas
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    # URL para visualizar detalhes de uma tarefa com base no 'pk'
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]