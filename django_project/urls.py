"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from api import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api_posts', api_views.PostsListViewSet,basename='api2')
router.register(r'user_register', api_views.UserRegisterViewSet,basename='register')
router.register(r'user_profile', api_views.ProfileViewSet, basename='profile')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name= 'blog-register'),
    path('profile/', user_views.profile, name= 'profile'),
    path('', include('blog.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    #API Views

    path('api/posts/', api_views.PostsList.as_view(), name='api-post-list'),
    path('api/user_posts/', api_views.UserPostsList.as_view(), name='users-posts-list'),
    path('api/register/', api_views.RegisterUser.as_view(), name='api_user_register'),
    path('api/user_profile/', api_views.UserProfileUpdate.as_view(), name='api_user_profile_data'),

    #routers
    path('api2/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)