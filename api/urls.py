from django.urls import path
from . import views

urlpatterns = [
    path('notes/info', views.get_routes_info, name='routes-info'),
    path('notes', views.note_list_and_create, name='notes'),
    path('notes/<str:pk>', views.note_detail_update_and_delete, name='notes-detail'),
]