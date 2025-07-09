from django.urls import path
from .views import SessionListCreateView, MediaUploadView, NoteCreateView, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sessions/', SessionListCreateView.as_view(), name='session-list-create'),
    path('media/', MediaUploadView.as_view(), name='media-upload'),
    path('notes/', NoteCreateView.as_view(), name='note-create'),
    path('register/', RegisterView.as_view(), name='register'),
] 