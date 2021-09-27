"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
       title='Store Infinity Manager API',
       default_version='1.0.0',
       description='API for the technical challenge'
  ),
  public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Project URLs
    path('',include('store.urls',namespace='store')),
    path('',include('user.urls',namespace='user')),
    # JWT
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    # Swagger
    url(r'^docs/$',schema_view.with_ui('swagger',cache_timeout=0),name='schema_swagger_ui')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
