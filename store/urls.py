from .views import *
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('',StoreView.as_view(),name='index'),
]
