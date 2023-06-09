from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from .models import User

from apps.cart.models import CartItem, Cart


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    title = '-E Shop - Авторизация'
    success_url = reverse_lazy('index')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'E Shop - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    title = 'E Shop - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    # def get_context_data(self, **kwargs):
    #     kwargs['carts'] = CartItem.objects.filter(user=self.object)
    #     return super().get_context_data(**kwargs)


class UserLogoutView(TitleMixin, LogoutView):
    title = 'E Shop - Выход'
    success_url = reverse_lazy('index')
