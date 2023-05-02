from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .models import *
from django.core.paginator import Paginator


def index(request):
    return render(request, "capstone/index.html")

def about(request):
    return render(request, "capstone/about.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")

# Profile page goes here
@login_required(login_url='/login')
def profile(request):
    playlist = Playlist.objects.filter(user=request.user.username)
    playlist_items = []
    saved = 0
    present_in_playlist = False
    if playlist:
        for item in playlist:
            try:
                game = Game.objects.get(id=item.game_id)
                playlist_items.append(game)
                present_in_playlist = True
                saved += 1
            except:
                present_in_playlist = False

    playinglist = Playinglist.objects.filter(user=request.user.username)
    playinglist_items = []
    playing = 0
    present_in_playinglist = False
    if playinglist:
        for item in playinglist:
            try:
                game = Game.objects.get(id=item.game_id)
                playinglist_items.append(game)
                present_in_playinglist = True
                playing += 1
                playinglist = Playinglist.objects.get(game_id=item.game_id, started_on=item.started_on)

            except:
                present_in_playinglist = False

    playedlist = Playedlist.objects.filter(user=request.user.username)
    playedlist_items = []
    finished = 0
    present_in_playedlist = False
    if playedlist:
        for item in playedlist:
            try:
                game = Game.objects.get(id=item.game_id)
                playedlist_items.append(game)
                present_in_playedlist = True
                finished += 1
                playedlist = Playedlist.objects.get(game_id=item.game_id)

            except:
                present_in_playedlist = False

    context = {
        "playinglist": playinglist,
        "playedlist": playedlist,
        "present_in_playlist": present_in_playlist,
        "playlist_items": playlist_items,
        "saved": saved,
        "present_in_playinglist": present_in_playinglist,
        "playinglist_items": playinglist_items,
        "playing": playing,
        "present_in_playedlist": present_in_playedlist,
        "playedlist_items": playedlist_items,
        "finished": finished
    }

    return render(request, "capstone/profile.html", context)

# Add game goes here
@login_required(login_url='/login')
def add_game(request):
    if request.method == "POST":
        game = Game()

        game.title = request.POST.get('title')

        if request.POST.get('description'):
            game.description = request.POST.get('description')
        else:
            game.description = "No description provided!"

        if request.POST.get('genre'):
            game.genre = request.POST.get('genre')
        else:
            game.genre = None

        if request.POST.get('platform'):
            game.platform = request.POST.get('platform')
        else:
            game.platform = None

        if request.POST.get('developer'):
            game.developer = request.POST.get('developer')
        else:
            game.developer = None

        if request.POST.get('publisher'):
            game.publisher = request.POST.get('publisher')
        else:
            game.publisher = None

        if request.POST.get('image'):
            game.image = request.POST.get('image')
        else:
            game.image = "https://upload.wikimedia.org/wikipedia/commons/4/46/Question_mark_%28black%29.svg"

        game.added_by = request.user.username
        
        game.save()

        games = Game.objects.all()
        empty = False
        if len(games) == 0:
            empty = True
        return redirect("games_list")
    else:
        return render(request, "capstone/add_game.html")
    
# Game list goes here
def games_list(request):
    games = Game.objects.all()
    empty = False
    if len(games) == 0:
        empty = True

    page_number = request.GET.get('page')
    page_obj = Paginator(games, 9).get_page(page_number)

    return render(request, "capstone/games_list.html", {
        "games": games,
        "empty": empty,
        "page_obj": page_obj
    })

# Specific game view goes here
def game_view(request, title, id):
    games = Game.objects.all()
    game = Game.objects.get(title=title, id=id)
    new_game = Playlist.objects.filter(game_id=id, user=request.user.username)
    playing_game = Playinglist.objects.filter(game_id=id, user=request.user.username)
    played_game = Playedlist.objects.filter(game_id=id, user=request.user.username)

    empty = False
    if len(games) == 0:
        empty = True
        
    return render(request, "capstone/game_view.html", {
        "games": games,
        "game": game,
        "new_game": new_game,
        "playing_game": playing_game,
        "played_game": played_game,
        "empty": empty
    })

# Edit function goes here
@csrf_exempt
@login_required(login_url='/login')
def edit(request, id):
    game = Game.objects.get(id=id)

    if request.method == "PUT":
        data = json.loads(request.body)
        game.description = data["description"]
        game.genre = data["genre"]
        game.platform = data["platform"]
        game.developer = data["developer"]
        game.publisher = data["publisher"]
        game.image = data["image"]
        if game.image == "":
            game.image = "https://upload.wikimedia.org/wikipedia/commons/4/46/Question_mark_%28black%29.svg"

        game.save()
        return redirect(reverse("games_list"))

# Delete function goes here
@login_required(login_url='/login')
def delete_game(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == "POST":
        game.delete()
        return redirect("games_list")
    else:
        return redirect('game_view', id=id)
    
# Playlist function goes here
@login_required(login_url='/login')
def add_to_playlist(request, game_id):
    obj = Playlist.objects.filter(game_id=game_id, user=request.user.username)

    if obj:
        obj.delete()
        game = Game.objects.get(id=game_id)
        new_game = Playlist.objects.filter(game_id=game_id, user=request.user.username)
        return redirect("profile")
    else:
        obj = Playlist()
        obj.user = request.user.username
        obj.game_id = game_id
        obj.save()
        game = Game.objects.get(id=game_id)
        new_game = Playlist.objects.filter(game_id=game_id, user=request.user.username)
        return redirect("profile")
    
# Playinglist function goes here
@login_required(login_url='/login')
def add_to_playinglist(request, game_id):
    obj = Playinglist.objects.filter(game_id=game_id, user=request.user.username)
    playing_game = Playinglist.objects.filter(game_id=game_id, user=request.user.username)
    game = Game.objects.get(id=game_id)

    if obj:
        obj.delete()
        game
        playing_game
        return redirect("profile")
    else:
        obj = Playinglist()
        obj.user = request.user.username
        obj.game_id = game_id
        obj.save()
        game
        playing_game

        return redirect("profile")
    
# Playedlist function goes here
@login_required(login_url='/login')
def add_to_playedlist(request, game_id):
    obj = Playedlist.objects.filter(game_id=game_id, user=request.user.username)
    played_game = Playedlist.objects.filter(game_id=game_id, user=request.user.username)

    if obj:
        obj.delete()
        game = Playinglist.objects.get(game_id=game_id)
        played_game
        return redirect("profile")
    else:
        obj = Playedlist()
        obj.user = request.user.username
        obj.game_id = game_id
        obj.save()
        
        game = Playinglist.objects.get(game_id=game_id)
        game.delete()

        played_game
        
        return redirect("profile")