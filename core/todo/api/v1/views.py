from .serializers import TaskSeializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from todo.models import Task




class TaskModelViewSt(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSeializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)   


    



