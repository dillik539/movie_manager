from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    return render(request, 'movie_management_app/homepage.html')

def popularMovies(request):
    return render(request, 'movie_management_app/popular_movies.html')

# def login(request):
#     return render(request, 'movie_management_app/login.html')
#
# def logout(request):
#     return redirect(request, 'movie_management_app/homepage.html')

def my_profile(request):
    return render(request, 'movie_management_app/my_profile.html')

# def register(request):
#     return render(request, 'movie_management_app/register.html')

def user(request):
    return render(request, 'movie_management_app/user.html')

def watch_list(request):
    return render(request, 'movie_management_app/watchlist.html')

def watched_list(request):
    return render(request, 'movie_management_app/watchedlist.html')
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('homepage')

        else :
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html', { 'form' : form , 'message' : message } )


    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', { 'form' : form } )
