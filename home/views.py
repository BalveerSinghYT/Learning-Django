from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# password for user veer is Veer$$@@

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        secret = request.POST.get('password')
        # Check if user entered correct credential.
        user = authenticate(username = username, password = secret)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
         
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')