"""config URL Configuration

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
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import AccountCreateRetrieveViewSet, AccountView

from auths.views import OAuthTokenObtainView
from profiles.views import ProfileRetrieveUpdateView
from programs.views import ProgramViewSet

account_router = DefaultRouter()
account_router.register(
    r'accounts', AccountCreateRetrieveViewSet, basename='accounts')

program_router = DefaultRouter()
program_router.register(r'program', ProgramViewSet, basename='program')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/<str:provider>/token',
         OAuthTokenObtainView.as_view(), name='token_obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('accounts/', AccountCreateRetrieveView.as_view()),

    path('', include(program_router.urls)),
    path('', include(account_router.urls)),

    path('profile/<int:id>/', ProfileRetrieveUpdateView.as_view(), name='profile'),
]
