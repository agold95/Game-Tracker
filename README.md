# Game Tracker

### Description
Game Tracker is an app that lets users track the video games they want to play, the games they are playing, and the games they have played. The app allows users to add games into a database, view all the games added by every user, edit the games they have added, and delete them from the database if necessary. When A user finds a game they would like to play, they can add that game to their own personal playlist. Then, if they are ready to start playing it, they can add that game into the list of games they are playing. Once they have completed a game, they can then add that completed game to their list of completed games. 

The app is useful for keeping tabs and track of all the games the user has played, and can effectively be scaled to a wider number of users. Each game created has its own unique entry into the database, and contains fields for information about the game, such as the game’s description, genre, platform, publisher, and developer, as well as any box-art released for the game. All these fields are changeable (except for the title) as long as the user who created the entry is valid.

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
