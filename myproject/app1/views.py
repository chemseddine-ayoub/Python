from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Welcome</h1>')
    name = 'Yassine'
    context = {
        'name' : 'Chemseddine',
        'age' : 20 ,
        'morrocan' : 'True'
    }
    return render(request, 'index.html' , context)

def counter(request):
    if request.method == 'POST': 
        text = request.POST.get('txt')
        amount_of_words = len(text.split())
        return render(request,'counter.html',{'amount':amount_of_words})
    return render(request , 'counter.html')

def display(request):
    data = Feature.objects.all()
    return render(request , 'index.html' , {'data' : data})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =  request.POST.get('password')
        password1 =  request.POST.get('password1')
        if password == password1 :
            if User.objects.filter(email = email).exists():
                messages.info(request , 'email existe deja')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request , 'username existe deja')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username , email=email , password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request , 'MDP non identiques')
            return redirect('register')
    else:
        return render(request , 'register.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request , 'Cred invalid')
            return redirect('index')
    else:
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')