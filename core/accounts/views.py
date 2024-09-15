from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, RedirectView
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin




class LoginPageView(LoginView):
    template_name = 'accounts/login.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task_list")


class RegisterPageView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('todo:task_list')
    redirect_authenticated_user = True


    def form_valid(self, form):
        user = form.save()
        if user is not None:
           login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super(RegisterPageView, self).get(*args, **kwargs)



class LogoutPageView(LoginRequiredMixin, RedirectView):
    url = '/'

    def get(self, request):
        logout(request)
        return redirect(self.url)