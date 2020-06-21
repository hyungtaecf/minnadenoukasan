from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'blog'

urlpatterns = [
    path('',views.PostList.as_view(),name='post_list'),
    path('article/<slug:slug>',views.PostDetail.as_view(),name='post_detail'),
    path('new_article/',staff_member_required(views.PostCreate.as_view()),name='post_create'),
    path('article/<slug:slug>/edit',staff_member_required(views.PostUpdate.as_view()),name='post_update'),
    path('article/<slug:slug>/delete',staff_member_required(views.PostDelete.as_view()),name='post_delete'),
]
