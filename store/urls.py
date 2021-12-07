from django.urls import path
from .views import StoreDelete, StoreDetail, StoreEdit, StoreList, StoreListDetailFilter, StoreOwnerDetail

app_name = 'store'

urlpatterns = (
    path('store/',StoreList.as_view(),name='storecreate'),
    path('search/',StoreListDetailFilter.as_view(),name='storesearch'),
    path('store/<int:pk>/',StoreEdit.as_view(),name='storeedit'),
    path('store/owner/<int:pk>/',StoreOwnerDetail.as_view(),name='storeownerdetail'),
    path('store/delete/<int:pk>/',StoreDelete.as_view(),name='storedelete'),
    path('store/<str:pk>/',StoreDetail.as_view(),name='storedetail')
)
