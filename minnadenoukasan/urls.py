"""minnadenoukasan URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from .views import edit_profile
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='index'),
    path('message_sent/',views.MessageSent.as_view(),name='message_sent'),
    path('search_result/',views.SearchView.as_view(),name='search_result'),
    path('news/', include('blog.urls', namespace='blog')),
    path('gallery/',include('gallery.urls', namespace='gallery')),
    path('store/',include('store.urls',namespace='store')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.Profile.as_view(), name='profile'),
    path('accounts/profile/edit/', edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
