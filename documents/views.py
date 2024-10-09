from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from rest_framework import permissions
from documents.models import Document, DocumentComment
from .serializers import (
    DocumentListDetailSerializer,
    DocumentCreateUpdateSerializer,
    
    DocumentCommentSerializer,
)


##### GET ALL DOCUMENT VIEWS
class DocumentsListAPIView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentListDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)
    
    
##### CREATE DOCUMENT VIEWS
class DocumentCreateAPIView(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_serializer_context(self):
        return {
            'user_id': self.request.user
        }
    

##### DOCUMENT DETAILED VIEWS
class DocumentDetailAPIView(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentListDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)


##### DOCUMENT UPDATE VIEWS
class DocumentUpdateAPIView(UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateUpdateSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {
            'user_id': self.request.user
        }
        
        
##### DOCUMENT DELETE VIEWS
class DocumentDeleteAPIView(DestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentListDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)


##### DOCUMENT COMMENT API VIEW
class DocumentCommentListCreateView(ListCreateAPIView):
    queryset = DocumentComment.objects.all()
    serializer_class = DocumentCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        document_id = self.kwargs.get('document_id')
        return DocumentComment.objects.filter(document_id=document_id)
    
    def perform_create(self, serializer):
        document_id = self.kwargs.get('document_id')
        document = get_object_or_404(Document, id=document_id)
        # if DocumentComment.objects.filter(document=document, user=self.request.user).exists():
        #     return serializers.ValidationError({'detail': 'You already Commented on this Document'})
        serializer.save(user=self.request.user, document=document)