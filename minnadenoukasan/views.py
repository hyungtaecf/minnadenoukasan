# PROJECT VIEWS.PY
from .forms import QandAForm, UserEditForm
from django.db.models import Q
from django.views.generic import TemplateView, UpdateView, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.core.mail import EmailMessage
from blog.models import Post
from gallery.models import GalleryImage
from gallery.views import displayingItemsNumber
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.admin import EmailAddress
from django.shortcuts import get_object_or_404

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def home(request):
    print("--INFO: "+get_ip(request)+" visited Agrevo Life's Homepage") # prints the visitor's ip
    qAndA_form = QandAForm

    if request.method == 'POST':
        form = qAndA_form(data=request.POST)

        if form.is_valid():
            template = get_template('qAndA_form.txt')
            content = {
                'name' : request.POST.get('name'),
                'email' : request.POST.get('email'),
                'question' : request.POST.get('question'),
            }
            content = template.render(content)
            email = request.POST.get('email')
            email = EmailMessage(
                "New Q&A form email",
                content,
                "Agrevo Life",
                ['info@agrevo.life'],
                headers = { 'Reply To': email}
            )
            email.send()
            return redirect('message_sent')

    context = {
        'qAndA_form':qAndA_form,
        # 'most_recent':Post.objects.order_by('-publish_date'),
        'gallery':GalleryImage.objects.all()[:displayingItemsNumber],
        'article_1':get_object_or_404(Post, slug='recruitment-of-fields-for-freeze-thaw-awakening-technology'),
        'article_2':get_object_or_404(Post, slug='japan-s-technology-to-avoid-a-worldwide-food-crisis'),
    }
    return render(request, 'index.html', context)

class SearchView(View):
    def get(self, request, *args, **kwargs):
        template = 'search_result.html'
        input = request.GET.get('search_input')
        result = Post.objects.filter(Q(title__icontains=input) | Q(text__icontains=input))
        showGoToLogin = input == "login"

        context = {
            'result': result,
            'input': input,
            'showGoToLogin': showGoToLogin,
        }
        return render(request,template,context)

class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'staff/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        email_verified = EmailAddress.objects.filter(user=context['view'].request.user, verified=True).exists()
        context.update({'email_verified':email_verified})
        return context

class MessageSent(TemplateView):
    template_name = 'message_sent.html'

class UserEditView(UpdateView):
    """Allow view and update of basic user data.
    In practice this view edits a model, and that model is
    the User object itself, specifically the names that
    a user has.
    The key to updating an existing model, as compared to creating
    a model (i.e. adding a new row to a database) by using the
    Django generic view ``UpdateView``, specifically the
    ``get_object`` method.
    """
    form_class = UserEditForm
    template_name = "staff/edit_profile.html"
    view_name = 'edit_profile'
    success_url = reverse_lazy(view_name)

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'User profile updated')
        return super(UserEditView, self).form_valid(form)

edit_profile = login_required(UserEditView.as_view())
