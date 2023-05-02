
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("add_game", views.add_game, name="add_game"),
    path("games_list", views.games_list, name="games_list"),
    path("game_view/<str:title>/<int:id>", views.game_view, name="game_view"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete_game/<int:id>", views.delete_game, name="delete_game"),
    path("add_to_playlist/<int:game_id>", views.add_to_playlist, name="add_to_playlist"),
    path("add_to_playinglist/<int:game_id>", views.add_to_playinglist, name="add_to_playinglist"),
    path("add_to_playedlist/<int:game_id>", views.add_to_playedlist, name="add_to_playedlist")
]