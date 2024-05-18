from django.urls import path
from .views import TaskAPI, TaskDetailsAPI


urlpatterns = [
    path('assign/', TaskAPI.as_view()),
    path('detail/<int:pk>/', TaskDetailsAPI.as_view()),
]


