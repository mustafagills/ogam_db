from django.urls import path, include
from . import views as Users_view

app_name = 'users'

urlpatterns =[
    path('signup/', Users_view.signup_view, name ='signup'),
    path('login/', Users_view.login_view, name ='login'),
    path('logout/', Users_view.logout_view, name ='logout'),
]
