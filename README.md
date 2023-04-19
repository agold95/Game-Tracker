# Game Tracker

### Description
Game Tracker is an app that lets users track the video games they want to play, the games they are playing, and the games they have played. The app allows users to add games into a database, view all the games added by every user, edit the games they have added, and delete them from the database if necessary. When A user finds a game they would like to play, they can add that game to their own personal playlist. Then, if they are ready to start playing it, they can add that game into the list of games they are playing. Once they have completed said game, they can then add that completed game to their list of completed games. 

The app is useful for keeping tabs and track of all the games the user has played, and can effectively be scaled to a wider number of users. Each game created has its own unique entry into the database, and contains fields for information about the game, such as the game’s description, genre, platform, publisher, and developer, as well as any box-art released for the game. All these fields are changeable (except for the title) as long as the user who created the entry is valid.

### Distinctiveness and Complexity
One of the ways this project is distinct from the other projects in this course is because it closely follows and expands on the principles of a CRUD app in that the user is able to create data, read that data, update it when they choose, and delete it when necessary, all while having a clean, simple, and easy-to-use user interface that allows the user to do so. I made it easy for a user to add new games to the database, and included several fields for them to input data based on the game. Each game is added to the `Games` database where that data is then displayed on the `games_list.html` page where every user can read about that specific game.

Another layer of complexity was in how `games_list.html` was rendered. I wanted to only show some but not all of the games in the database at a time so I decided to use page pagination and bootstrap's built-in grid system to do so, and so decided 3x3 column/row would keep each page simple and easy to read. To render each card while also maintaining the page pagination, I wrapped opening and closing `div` tags in a Django `forloop.counter0` which will get the current iteration starting at 0, then divided that by 3. This would render each card in the parent `div`, then the `forloop.last` would divide those cards based on the last card in that parent div and render the closing tag to complete the pagination. All this can be seen in the `gameslist.html` template.

Another aspect of complexity in this project is the url path to `game_view.html`. I decided it would better suit the database and be easier to access if that url path was concatenated with both the title of the game that was added and also the specific `id` that is generated in the Django model. By doing so this way, it allows users to add games to the database with the same title but still keeps them distinct by `id`, since there are numerous games that are different but may have the [same title](https://www.giantbomb.com/same-name-different-game/3015-5521/). It also keeps the url more readable, since having a path to `/title` is easier to read and understand for the user rather than just a path using `/id` that contains the integer of the `id`. 

An additional complexity is in addition to a user being able to create and read a game in the database, I made it very simple for them to update that game using javascript to replace almost every field and save it to the database. The javascript code in the `edit` function in `main.js` also allows the all the data that was initially input by the user to remain in the editable text box/field, so the user can make simple changes without having to input all the data again. The only input field that is unchangeable is the game's 'title' field, since this and also its generated `id` are tied directly into how the game is accessed in the url path to `game_view.html`. If there is a mistake in the title, the user who created that entry can very easily delete the game from the database with the use of the `delete_game` function in `views.py`. And to be sure the user deleting the game is absolutely sure they want to delete the game I added the `delete_confirmation` function in `main.js` which will return a confirmation box with an option to cancel before actually removing the game from the database.

Another aspect that makes this project complex is the use of databases that move games in each list of a respective user between one another. In addition to the `Game` database I created three different databases to handle moving a game from list to list between the `Playlist` database, `Playinglist`, and `Playedlist`. As seen in `views.py` in the `add_to_playlist`, `add_to_playinglist`, and `add_to_playedlist` functions, each of these will add the data from from the current database into the destination database, then delete that game from its database. So if a user added a game to their `playedlist`, it will take the database entry for that game from their `playinglist`, and then delete that game from their `playinglist`, essentially stringing along each game between databases. And once a user move items between databases, the `profile` function in `views.py` will count the number of games in that list, so a user could keep track of the number.



### Files
	capstone – main project folder
    
		static – contains the images I used as well as the main javascript file and css file.
        	images - Main images used in creating the app.
			main.js – contains the javascript functions for editing an entry in the database as well as deleting an entry in the database.    
			styles.css – main css styling.
            
		templates – contains all the html templates used in the app.
            about.html – an about web page section instructing the user on how to use the app.
            add_game.html – the html view that allows registered users to enter a game into the database.
            game_view.html – the view and structure for how each individual entry in the game database looks. Lists specific aspects that the user can fill in to describe the game, like a description, genre, publisher, etc.
            games_list.html – the full list of games in the database, complete with page pagination.
            index.html – the entry page for running the app, contains info on how to get started.
            layout.html – the main layout of each page, allows users to easily navigate between different pages of the app, used in each subsequent web page.
            login.html – login page for users.
            profile.html – The main profile view for the users. Here the user can see all three playlists and how they are tracking the respective games in said playlists.
            register.html – page for registering new users.
            
        admin.py – models for allowing superusers into the admin section of the app.
        models.py – All the models used for the app. Contains models for users, games, and the user’s playlists.
        urls.py – url paths for all views and routes.
        views.py -  the main backend python code for the app. 
        db.sqlite3 – the main generated database for all models of the app.

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