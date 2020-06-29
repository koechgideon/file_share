from django.urls import path
from filebox import views
from filebox.views import (UploadListView,
                           UploadDetailView,
                           UploadCreateView,
                           UploadUpdateView,
                           UploadDeleteView,
                           UserUploadListView)

 

urlpatterns = [
    path('', views.home, name='main-home'),
    path('application', UploadListView.as_view(), name='filebox-home'),
    path('user/<str:username>', UserUploadListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', UploadDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', UploadUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', UploadDeleteView.as_view(), name='post-delete'),
    path('post/new/', UploadCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='filebox-about'),
]