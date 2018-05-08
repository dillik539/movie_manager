from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^popularmovies/$', views.popularMovies, name = 'popular_movies'),
    url(r'^myprofile/$', views.my_profile, name = 'my_profile'),
    url(r'^user/$', views.user, name = 'user'),
    url(r'^user/movies/watchlist/$', views.watch_list, name = 'watch_list'),
    url(r'^user/movies/watchedlist/$', views.watched_list, name = 'watched_list'),
    url(r'^user/movies/movielist/$', views.movie_list, name = 'movie_list'),
    url(r'^user/movies/wishlist/$', views.add_to_watchlist, name = 'add_to_watchlist'),
    url(r'^user/movies/watchedmovie/$', views.add_to_watchedlist, name = 'add_to_watchedlist'),
    url(r'^user/movies/moviedetail/(?P<pk>\d+)/$', views.movie_detail, name = 'movie_detail'),
]
