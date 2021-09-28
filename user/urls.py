from django.urls import path

from .views import CustomUserCreate, CustomUserView, decorated_login_view

app_name = 'user'

urlpatterns = (
    path('user/create/',CustomUserCreate.as_view(),name='create_user'),
    path('user/delete/',CustomUserView.as_view(),name='delete_edit_user'),
    path('login/',decorated_login_view,name='token_obtain_pair'),
)
