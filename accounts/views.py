from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from .forms import UserRegisterForm

User = get_user_model()


class UserRegisterView(FormView):
    template_name = 'registration/registration_form.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = None

    def get_object(self, **kwargs):
        return get_object_or_404(
            User,
            username__iexact=self.kwargs.get("username")
        )

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        return context
