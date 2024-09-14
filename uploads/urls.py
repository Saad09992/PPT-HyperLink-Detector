from django.urls import path
from uploads.views import upload_file, list_files, process_pptx, save_guide, list_guides, user_files, delete_file

urlpatterns = [
    path('upload/<int:user_id>/', upload_file, name='upload_file'),
    path('files/', list_files, name='list_files'),
    path('guides/save/', save_guide, name='save_guide'),
    path('guides/', list_guides, name='list_guides'),
    path('process-pptx/<int:file_id>/', process_pptx, name='process_pptx'),
    path('user/<int:user_id>/files/', user_files, name='user_files'),
    path('user/<int:user_id>/files/<int:file_id>/delete/', delete_file, name='delete_file'),
]