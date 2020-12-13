from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from home.models import registeration
# password for user veer is Veer$$@@

# Create your views here.

def index(request):
    context = {
        'display_logout': 'Logout'
    }
    
    if request.user.is_authenticated:
        print("Logged in")
        return render(request, 'index.html', context)
    else:
        print("Not logged in")
        return render(request, 'index.html')

    #if request.user.is_anonymous:
    #    return redirect('/login')
    #return render(request, 'index.html')

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

def Registeration(request):
    return render(request, 'registeration.html')

def base(request):
    return render(request, 'base.html')

def records(request):
    data = registeration.objects.all()
    print(data)
    return render(request, 'records.html', {'data': data})