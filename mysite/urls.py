"""mysite URL Configuration

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
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from myAnimations import views as myAnimation_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('myAnimations/',include('myAnimations.urls')),
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/create',user_views.profile,name='profile'),
    path('profile/view',user_views.profileView,name='profile_view'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('ajax_datatable/permissions/', myAnimation_views.PermissionAjaxDatatableView.as_view(), name="ajax_datatable_permissions"),
    path('', myAnimation_views.index),
    path('activate/<uidb64>/<token>', user_views.activate,name='activate'),

    path('password_reset/',authentication_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset/done/',authentication_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',authentication_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',authentication_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

    
]
urlpatterns += []+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


