from django.shortcuts import render, redirect
from .forms import RegistrationForm, WatchedListForm, WatchListForm, PopularMoviesForm
from django.contrib.auth import authenticate, login, logout
import requests
from movie_management_app import movie_data
from .models import WatchList


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
    # apikey = 'd14fee3e'

    # if 'search_movie' in request.GET:
    #     title = request.GET.get('search_movie')
    #     print(title)
    #     url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+title
    #     response = requests.get(url)
    #     movie = response.json()['Title']
    # else:


    title = request.GET.get('search_movie')
    movie = movie_data.get_movie_info(title)

    # print(title)
    # url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+title
    # response = requests.get(url)
    # movie = response.json()
    #
    # title = movie['Title']
    # year = movie['Year']
    # released = movie['Released']


    return render(request, 'movie_management_app/movie.html',{'movie': movie})

def add_to_watchlist(request):

    title = request.POST.get("Title")
    year = request.POST.get('Year')
    director = request.POST.get('Director')
    actor = request.POST.get('Actors')
    new_movie = WatchList(name = title, actor = actor, director = director, year = year)
    # new_movie = WatchList(name = movie.Title, actor = movie.Actors, director = movie.Director, year = movie.Year)
    if not 'Cancel' in request.POST:
        new_movie.save()
    return render(request, 'movie_management_app/user.html')



def watched_list(request):
    form = WatchedListForm()
    search_movie = request.GET.get('search_movie')
    return render(request, 'movie_management_app/watchedlist.html', {'form': form})

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
