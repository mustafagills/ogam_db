from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.views.generic import CreateView, FormView
from django.utils.http import is_safe_url
#from django.contrib.auth.decorators import login_required

# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/signup.html'
    success_url = '/users/login/'

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username = email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['email']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        return super(LoginView, self).form_invalid(form)
# def signup_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = RegisterForm()
#     return render(request, 'users/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user() #retrieves the user in the form
#             login(request, user)
#             return redirect('/')
#
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
