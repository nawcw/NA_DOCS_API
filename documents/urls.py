from django.urls import path
from .views import (
    DocumentsListAPIView,
    DocumentCreateAPIView,
    DocumentDetailAPIView,
    DocumentUpdateAPIView,
    DocumentDeleteAPIView,
    
    DocumentCommentListCreateView,
    )


urlpatterns = [
    path('', DocumentsListAPIView.as_view(), name='all-documents'),
    path('create/', DocumentCreateAPIView.as_view(), name='create-document'),
    path('<id>/detail', DocumentDetailAPIView.as_view(), name='document-detail'),
    path('<id>/update/', DocumentUpdateAPIView.as_view(), name='document-update'),
    path('<id>/delete/', DocumentDeleteAPIView.as_view(), name='document-delete'),
    
    path('comments/<int:document_id>/', DocumentCommentListCreateView.as_view(), name='document-comments'),
]