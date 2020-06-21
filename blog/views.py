from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from .models import Post
from .forms import PostForm
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from minnadenoukasan.views import get_ip

# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 5
    allow_empty = False #Throws 404 if there is no Posts

    def listing(request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 5)

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        print("--INFO: "+str(context['view'].request.user)+" entered News Page using the IP: "+ str(get_ip(context['view'].request)))
        most_viewed = Post.objects.order_by('-hit_count_generic__hits','-publish_date')
        has_previous_3pages = context["page_obj"].number > 3
        has_previous_2pages = context["page_obj"].number > 2
        has_next_2pages = context["paginator"].num_pages - context["page_obj"].number > 1
        has_next_3pages = context["paginator"].num_pages - context["page_obj"].number > 2
        context.update({
            'most_viewed':most_viewed,
            'has_previous_3pages':has_previous_3pages,
            'has_previous_2pages': has_previous_2pages,
            "has_next_2pages": has_next_2pages,
            "has_next_3pages":has_next_3pages})
        return context

    def get_queryset(self):
        for post in Post.objects.all():
            return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')

class PostDetail(HitCountDetailView):
    model = Post
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context.update({
        'most_viewed': Post.objects.order_by('-hit_count_generic__hits')[:2],
        })
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'author', 'image','text']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug' : self.object.slug})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreate, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'author', 'image','text']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug' : self.object.slug})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostUpdate, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
