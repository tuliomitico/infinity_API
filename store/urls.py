from django.urls import path
from .views import StoreDelete, StoreDetail, StoreEdit, StoreList, StoreOwnerDetail

app_name = 'store'

urlpatterns = (
    path('store/',StoreList.as_view(),name='storecreate'),
    path('store/<int:pk>/',StoreEdit.as_view(),name='storeedit'),
    path('store/owner/<int:pk>/',StoreOwnerDetail.as_view(),name='storeownerdetail'),
    path('store/<int:pk>/',StoreDelete.as_view(),name='storedelete'),
    path('store/<str:pk>/',StoreDetail.as_view(),name='storedetal')
)
