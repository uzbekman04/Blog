from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.NewPostView.as_view(), name='new'),
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditPostView.as_view(), name='edit'),
    path('<int:pk>/delete', views.DeletePostView.as_view(), name='delete'),
]