from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_message, name='create_message'),
    path('read/', views.read_messages, name='read_messages'),
    path('update/<int:message_id>/', views.update_message, name='update_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]
