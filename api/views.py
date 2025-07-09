from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Session, Media, Note
from .serializers import SessionSerializer, MediaSerializer, NoteSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class SessionListCreateView(generics.ListCreateAPIView):
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MediaUploadView(generics.CreateAPIView):
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        session_id = self.request.data.get('session')
        session = Session.objects.get(id=session_id, user=self.request.user)
        serializer.save(session=session)

class NoteCreateView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        session_id = self.request.data.get('session')
        session = Session.objects.get(id=session_id, user=self.request.user)
        serializer.save(session=session)

class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED) 