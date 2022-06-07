from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User, Customer, Owner
from .forms import CustomerForm, OwnerForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# Create your views here.

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        
        html_content=render_to_string('user/email.html', dict)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()      
        return redirect('/garage/index')

class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        
        user = form.save()
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content=render_to_string('user/email.html', dict)
        text_content = strip_tags(html_content)
        msg= EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()      
        
        return redirect('/garage/index')



class UserLoginView(LoginView):
    template_name = 'user/user_login.html'

class UserLogoutView(LogoutView):
    success_url = '/user/logout'


       

class UserListView(ListView):
    model = User
    users = User.objects.all()
    context_object_name = 'users'
    template_name = "user/user_list.html"
    ordering = ['id']

class UserDetailView(DetailView):
    model = User
    user = User.objects.all()
    context_object_name = 'user'
    template_name = "user/user_detail.html"


class UserDeleteView(DeleteView):
    model = User
    template_name = "user/user_delete.html"
    success_url = '/user/userlist'

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'profile_pic']
    template_name = "user/user_update.html"
    success_url = '/user/userlist'

def index(request):
    return render(request, 'user/index.html')