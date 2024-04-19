from decouple import config
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from rest_framework.authtoken.models import Token

from .forms import SendEmailMessageForm, UpdatePostsForm
from .models import Picture
from .tasks import send_email_to_author
from .tasks import update_posts


def index(request):
    pictures = cache.get_or_set(config('PICTURES_CACHE_NAME'),
                                Picture.objects.filter(~Q(categories=None)).prefetch_related(
                                    'categories').select_related('picture_post'))
    theme: str = request.COOKIES.get('theme')
    if request.method == 'POST':
        form = SendEmailMessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = f'Пользователь {cd["name"]} отправил сообщение: {cd["message"]} с почтой {cd["email"]} для обратной связи'
            print(type(cd['email']))
            send_email_to_author.delay(message, cd['email'])
    else:
        form = SendEmailMessageForm()
    return render(request, "blogsite/index.html", {"pictures": pictures, "form": form, "theme": theme})


class AdminPageView(FormView):
    form_class = UpdatePostsForm
    template_name = 'blogsite/adminpage.html'
    success_url = reverse_lazy('adminpage')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        token = Token.objects.get_or_create(user=self.request.user)
        update_posts.delay(str(list(token)[0].key))
        messages.success(self.request, "Посты успешно обновлены")
        return super().form_valid(form)
