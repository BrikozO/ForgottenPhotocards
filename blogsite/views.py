from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin
from rest_framework.authtoken.models import Token

from .forms import SendEmailMessageForm, UpdatePostsForm
from .models import Picture
from .tasks import send_email_to_author
from .tasks import update_posts


class MainPageView(FormMixin, ListView):
    model = Picture
    template_name = 'blogsite/index.html'
    context_object_name = 'pictures'
    form_class = SendEmailMessageForm

    def form_valid(self, form):
        cd = form.cleaned_data
        message = f'Пользователь {cd["name"]} отправил сообщение: {cd["message"]} с почтой {cd["email"]} для обратной связи'
        send_email_to_author.delay(message, cd['email'])
        return super().form_valid(form)

    def get_queryset(self):
        return Picture.objects.filter(~Q(categories=None))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme'] = self.request.COOKIES.get('theme')
        return context


class AdminPageView(FormView):
    form_class = UpdatePostsForm
    template_name = 'blogsite/adminpage.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        token = Token.objects.get_or_create(user=self.request.user)
        update_posts.delay(str(list(token)[0].key))
        messages.success(self.request, "Посты успешно обновлены")
        return super().form_valid(form)
