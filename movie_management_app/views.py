from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, WatchedListForm, WatchListForm, PopularMoviesForm
from django.contrib.auth import authenticate, login, logout
import requests
from movie_management_app import movie_data
from .models import WatchList, WatchedList


# Create your views here.
def homepage(request):
    return render(request, 'movie_management_app/homepage.html')

def popularMovies(request):
    form = PopularMoviesForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_management_app/popular_movies.html', {'form': form})

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
    watchlist = WatchList.objects.all()
    form = WatchListForm()
    search_movie = request.GET.get('search_movie')
    args = {'form' : form, 'watchlist': watchlist}
    return render(request, 'movie_management_app/watchlist.html', args)

def movie_list(request):
    title = request.GET.get('search_movie')
    movie = movie_data.get_movie_info(title)
    return render(request, 'movie_management_app/movie.html',{'movie': movie})

def add_to_watchlist(request):

    title = request.POST.get("Title")
    year = request.POST.get('Year')
    director = request.POST.get('Director')
    actor = request.POST.get('Actors')
    new_movie = WatchList(name = title, actor = actor, director = director, year = year)
    # new_movie = WatchList(name = movie.Title, actor = movie.Actors, director = movie.Director, year = movie.Year)
    movie_name = WatchList.objects.filter(name__iexact = title).all()
    if movie_name:
        message = 'That movie already exist in your database'
        return render(request, 'movie_management_app/watchlist.html', {'message': message})
    else:
        new_movie.save()
    return render(request, 'movie_management_app/user.html')


def add_to_watchedlist(request):
    title = request.POST.get("Name")
    year = request.POST.get('Year')
    director = request.POST.get('Director')
    actor = request.POST.get('Actors')
    watched_movie = WatchedList(name = title, actor= actor, director = director, year = year)
    if not 'Cancel' in request.POST:
        watched_movie.save()
        movie = WatchList.objects.filter(name__iexact = title)
        movie.delete()
    return render(request, 'movie_management_app/user.html')


# def add_to_watchedlist(request):

def movie_detail(request, pk):
    movie_detail = get_object_or_404(WatchList, pk = pk)
    return render(request, 'movie_management_app/movie_detail.html', {'movie_detail': movie_detail})


def watched_list(request):
    watched_movie = WatchedList.objects.all()
    # watched_movie = get_object_or_404(WatchedList, pk = pk)
    form = WatchedListForm()
    search_movie = request.GET.get('search_movie')
    # if request.method =="POST":

    # title = request.POST.get("Name")
    # print(title)
    # year = request.POST.get('Year')
    # director = request.POST.get('Director')
    # actor = request.POST.get('Actors')
    # watched_movie = WatchedList(name = title, actor = actor, director = director, year = year)
    # # new_movie = WatchList(name = movie.Title, actor = movie.Actors, director = movie.Director, year = movie.Year)
    # if not 'Cancel' in request.POST:
    #     watched_movie.save()
    # # return render(request, 'movie_management_app/user.html')
    return render(request, 'movie_management_app/watchedlist.html', {'form' :form, 'watched_movie' : watched_movie})

# def get_watch_list(request):
#     watchlist = WatchList.Objects.orderby('name')
#     return render(request, 'movie_management_app/watchlist.html')

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
