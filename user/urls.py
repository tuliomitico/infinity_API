from user.views import CustomUserCreate
from django.contrib.auth import get_user_model
from django.urls import path
from .views import CustomUserCreate, CustomUserView

app_name = 'user'

urlpatterns = (
    path('user/create/',CustomUserCreate.as_view(),name='create_user'),
    path('user/delete/',CustomUserView.as_view(),name='delete_edit_user')
)