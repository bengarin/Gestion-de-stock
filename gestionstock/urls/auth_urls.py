from django.urls import path
from gestionstock.views.auth_views import LoginView , SingupView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SingupView.as_view(), name='signup'),
]
