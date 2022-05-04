from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from random import randint
from rockPaper.forms import RegisterUserForms, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = 'rockPaper/register.html'
    success_url = 'rock'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'rockPaper/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return '/'


def rock(request):
    context = {
        'title': 'Rock'
    }
    if request.POST.get('connect'):
        print(request.POST['connect_loby'])
    elif request.POST.get('create_loby'):
        number_lobbi = randint(100, 999)
        context['number_lobbi'] = number_lobbi
    return render(request, 'rockPaper/rock.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')
