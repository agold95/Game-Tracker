# Game Tracker

### Description
Game Tracker is an app that lets users track the video games they want to play, the games they are playing, and the games they have played. The app allows users to add games into a database, view all the games added by every user, edit the games they have added, and delete them from the database if necessary. When A user finds a game they would like to play, they can add that game to their own personal playlist. Then, if they are ready to start playing it, they can add that game into the list of games they are playing. Once they have completed said game, they can then add that completed game to their list of completed games. 

The app is useful for keeping tabs and track of all the games the user has played, and can effectively be scaled to a wider number of users. Each game created has its own unique entry into the database, and contains fields for information about the game, such as the game’s description, genre, platform, publisher, and developer, as well as any box-art released for the game. All these fields are changeable (except for the title) as long as the user who created the entry is valid.

### Distinctiveness and Complexity
This capstone project is distinct from the others in the course in that it relies heavily on the database structures I have created and their ability to move data and items between different databases. By chaining these databases together, I made the flow of data from one to the other simple and clean, which allows me and the user to group information in a way that is readable and easy to understand.

In this project I have created a growing database that can be easily expanded and an easy to use and understand user interface that allows users to interact with the app with minimal effort on their part. A great deal of care went into creating a user interface that would be simple, flexible, and informative.

### Files
	capstone – main project folder
    
		static – contains the images I used as well as the main javascript file and css file.
        	images - Main images used in creating the app.
			main.js – contains the javascript functions for editing an entry in the database as well as deleting an entry in the database.    
			styles.css – main css styling.
            
		templates – contains all the html templates used in the app.
            about.html – an about section instructing the user on how to use the app.
            add_game.html – the html view for adding a game into the database.
            game_view.html – the view and structure for how each individual entry in the game database looks.
            games_list.html – the full list of games in the database.
            index.html – the entry page for running the app, contains info on how to get started
            layout.html – the main layout of each page, allows users to easily navigate between different pages of the app.
            login.html – login page for users.
            profile.html – The main profile view for the users. Here the user can see all three playlists and how they are tracking the respective games in said playlists.
            register.html – page for registering new users.
            
        admin.py – models for allowing superusers into the admin section of the app.
        models.py – All the models used for the app. Contains models for users, games, and the user’s playlists.
        urls.py – url paths for all views and routes.
        views.py -  the main python code for the app. 
        db.sqlite3 – the main database for all the models.

### How to Run
1.	Make sure you have [Python](https://www.python.org/downloads/) installed.
2.	Make sure you have Django installed by installing pip [here](https://pip.pypa.io/en/stable/installing/).
3.	Once pip is installed run `pip3 install Django` in your terminal to download Django.
4.	Download all the files of the app and unzip if necessary.
5.	In your terminal, `cd` into the capstone directory.
6.	Run `python manage.py makemigrations capstone` to make the migrations for the app.
7.	Run `python manage.py migrate` to migrate all files to the database.
8.	To run the app run `python manage.py runserver`.
9.	Then type `http://127.0.0.1:8000/` into your web browser and hit enter.

### Demo
[https://youtu.be/XMCBKFBwZdw](https://youtu.be/XMCBKFBwZdw)