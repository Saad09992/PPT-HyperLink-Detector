from rest_framework import serializers
from .models import UploadedFile, HtmlContent
from datetime import datetime

class UploadedFileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    upload_date = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ['id', 'file_name', 'upload_date', 'file']  # Include 'file' if you need the file URL

    def get_file_name(self, obj):
        return obj.file.name.split('/')[-1]  # Extracting just the file name

    def get_upload_date(self, obj):
        return obj.uploaded_at.strftime('%Y-%m-%d')  # Formatting the date to exclude time

class HtmlContentSerializer(serializers.ModelSerializer):
    uploaded_file = UploadedFileSerializer(read_only=True)  # Make this read-only
    uploaded_file_id = serializers.PrimaryKeyRelatedField(
        queryset=UploadedFile.objects.all(), write_only=True, source='uploaded_file'
    )  # Allow uploading by file ID

    class Meta:
        model = HtmlContent
        fields = ['id', 'content', 'created_at', 'uploaded_file', 'uploaded_file_id']

    def create(self, validated_data):
        uploaded_file = validated_data.pop('uploaded_file')
        html_content = HtmlContent.objects.create(uploaded_file=uploaded_file, **validated_data)
        return html_content
