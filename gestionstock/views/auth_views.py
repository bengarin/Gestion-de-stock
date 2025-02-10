from django.shortcuts import  render , redirect
from django.http import HttpResponse
from django.views import View
from gestionstock.forms import LoginForm
from django.contrib.auth import login ,logout ,authenticate

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/auth/login.html")
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else :
            return render(request, "pages/auth/login.html", {'form': form})    
    

class SingupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/auth/signup.html")
    
    def post(self, request, *args, **kwargs):
        pass

