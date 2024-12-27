from django.urls import path

from .views import Tasklist, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, logout_view

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create') ,
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
]