from rest_framework import serializers
from .models import Document, DocumentComment
from django.urls import reverse



class DocumentCommentSerializer(serializers.ModelSerializer):
    document = serializers.StringRelatedField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = DocumentComment
        fields = "__all__"




class DocumentListDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Document
        fields = ['id', 'owner', 'document_title', 'document_body', 'created_at', 'modified_at', 'comments']

    def get_comments(self, obj):
        comments = DocumentComment.objects.filter(document=obj)[:3]
        request = self.context.get('request')
        return {
            "commets": DocumentCommentSerializer(comments, many=True).data,
            "all_comment_link": request.build_absolute_uri(reverse('document-comments', kwargs={'document_id': obj.id}))
        }




class DocumentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [ 'document_title', 'document_body']
        
    def save(self, **kwargs):
        user_id = self.context['user_id']
        if self.instance is not None:
            self.instance = self.update(self.instance, self.validated_data)
            return self.instance
        else:
            document = Document.objects.create(**self.validated_data, owner=user_id)
            return document


