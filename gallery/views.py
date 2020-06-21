from .forms import *
from .models import *
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, View

# Displaying gallery images each time in the Index Page
displayingItemsNumber = 7 # IMPORTANT: Should be the same as in gallery.js

class GalleryView(ListView):
    model=GalleryImage
    context_object_name = 'gallery'
    template_name='gallery/gallery.html'

class RetrieveImages(View):
    def get(self, request):
        # Gets via ajax the requested indexes expressed in javascript
        fromIndex = int(request.GET.get('fromIndex', None))
        toIndex = int(request.GET.get('toIndex', None))

        # Checking pagination position
        first_page = False
        last_page = False
        if fromIndex > GalleryImage.objects.all().count()-1: # Is it going to the First Page?
            first_page = True
            fromIndex = 0
            toIndex = displayingItemsNumber
        elif fromIndex < 0: # Is it going to the Last Page?
            last_page = True
            fromIndex = (GalleryImage.objects.all().count() -
                GalleryImage.objects.all().count()%displayingItemsNumber)
            toIndex = GalleryImage.objects.all().count()

        if toIndex > GalleryImage.objects.all().count(): # Is it the Last Page and not full?
            toIndex = GalleryImage.objects.all().count()

        slicedListOfImages = serializers.serialize("json",GalleryImage.objects.all().order_by('id')[fromIndex:toIndex])
        data = {
            'slicedListOfImages': slicedListOfImages,
            'fromIndex': fromIndex,
            'toIndex': toIndex,
        }
        return JsonResponse(data)

class UploadingImagesToTheGallery(FormView):
    form_class = MultipleImagesForm
    template_name = 'gallery/upload.html'
    success_url = reverse_lazy('gallery:index')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('image_field')
        if form.is_valid():
            for i in images:
                image = GalleryImage.objects.create(image=i)
                image.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
