# from django.contrib.auth.models import User
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return Response({'status': 'success', 'user': UserSerializer(user).data})
        else:
            return Response({'status': 'failure', 'error': 'Invalid credentials'})
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer