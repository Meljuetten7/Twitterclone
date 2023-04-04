from django.urls import URLPattern, path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('delete/<int:post_id>/',views.delete, name='delete'),
    path('like/<int:post_id>/',views.likes, name='like'),
]