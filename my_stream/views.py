from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from .form import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Media,Video
from django.contrib.auth import login,logout,authenticate
# Create your views here.

#gerer la page d'inscription
def inscription(request):
    if request.method == 'POST':
        form=User(request.POST)
        if form.is_valid():
            form.save()
            form.instance.email = form.cleaned_data['email']
            user = form.save()
            print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
            return redirect('connexion')
    else:
        form=User()
    return render(request,'inscription.html',{'form':form})
#gerer la page d'accueil
@login_required
def home(request):
    return render(request,'index.html')

#gerer la page de connexion
def connexion(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "nom ou mot de pass incorrect")
    return render(request, 'connexion.html')

#gerer la page de deconnexion
def deconnexion(request):
    logout(request)
    return redirect('connexion')

def add_photo(request):
    photo= Media.objects.all()
    if photo is not None:
        return render(request, 'photo.html', {'photo':photo})
    else:
        raise Http404('photo nexiste pas')
    
def add_video(request):
    videos= Video.objects.all()
    if videos is not None:
        return render(request, 'video.html', {'video':videos})
    else:
        raise Http404('photo nexiste pas')
