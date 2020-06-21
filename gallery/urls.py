from .views import *
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

app_name = 'gallery'

urlpatterns = [
    path('', GalleryView.as_view(), name='index'),
    path('ajax/retrieve', RetrieveImages.as_view(), name='ajax_retrieve'),
    path('upload/', staff_member_required(UploadingImagesToTheGallery.as_view()), name='upload'),
]
