from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import Task, TaskListSerializer, TaskCreateSerializer, TaskUpdateSerializer
from .permissions import IsManagerOrTeamLeader, IsTaskAssignedTo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
import logging
from rest_framework.response import Response

mylogger = logging.getLogger('django')
# errorlogger = logging.getLogger('django')


class TaskAPI(ListCreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrTeamLeader]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.status_code == 200:
            mylogger.info('Tasks Fetched Successfully')
        else:
            mylogger.error('Error Fetching Tasks')
        return response

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            mylogger.info('Task created successfully')
            return response
        except Exception as e:
            mylogger.error('Error creating task')
            return Response(data='error creating task', status=400)



class TaskDetailsAPI(RetrieveUpdateAPIView):
    serializer_class = TaskUpdateSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTaskAssignedTo]

    def detail(self, request, *args, **kwargs):
        try:
            response = super().detail(request, *args, **kwargs)
            mylogger.info('Task Detail Fetched successfully')
            return response
        except Exception as e:
            mylogger.error('Error creating task')
            return Response(data='error fetching all task', status=400)





