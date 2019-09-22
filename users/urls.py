from django.urls import path, include
from .views import RegisterView, LoginView, logout_view

app_name = 'users'

urlpatterns =[
    path('signup/', RegisterView.as_view(), name ='signup'),
    path('login/', LoginView.as_view(), name ='login'),
    path('logout/', logout_view, name ='logout'),
]
