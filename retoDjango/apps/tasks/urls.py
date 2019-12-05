from django.urls import path
from .views import generate_users,UserListView,UserEditView,UserDeleteView

urlpatterns = [
    path('',generate_users,name='generate'),
    path('list/',UserListView.as_view(),name='list'),
    path('edit/<int:pk>/',UserEditView.as_view(),name='edit'),
    path('delete/<int:pk>/',UserDeleteView.as_view(),name='delete')
]
