# Udacity Fullstack ND Project 2
This application provides a webserver that accesses a database to provide the user with a selection of
books in the database organized by categories.   The website will allow users to log in through Facebook and add their own categories and books to the collection, with the ability to then edit or delete those entries afterward.

The website starts at a homepage which will list on the left the different categories in the database, and the list of books in the database in the center.
If a user selects a category, the website will return a page that lists the books for that particular category.  If a user selcts a book, the webpage will
return a page that displays the book title, and an in-depth description of the book.  When a user is logged in, buttons for Creating, Updating, or Deleting
content will be provided where applicable.

# Installation
This application was designed to run on the Udacity Fullstack ND VM, which can be downloaded [here](https://github.com/JeremySpradlin/fullstack-nanodegree-vm).  Instructions for installing and running the Fullstack ND VM can be found in the repositories README.md.

#### Application requirements if not using the Udacity VM
If you wish to run this application on a system other than the provided Udacity VM,  you will need to download and install the required packages for use in the application.  These are listed below with links to download.
- [Python 2.7.12](https://www.python.org/downloads/release/python-2712/)
- [Flask](http://flask.pocoo.org)
- [SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)
- [HttpLib2](https://pypi.org/project/httplib2/)
- [Python Open SSL](https://pyopenssl.org/en/stable/install.html)

#### Installation of web server
###### Setup and configure Database
To use the web application, you must first setup and configure the database.
```
python database_setup.py
python load_database.py
```

#### Starting the webserver
###### Configure App ID and Secret
For the app to use Facebook authentication, the application ID and Secret must in placed 
into a `fb_client_secrets.json` file.  The file must be created in the project directory, 
and the App_ID and App_Secret will be provided in the submission notes.

###### Running the server
Once the database has been setup and configured, run the following command to start the webserver
```
python application.py
```

#### Accessing the webpage
Once the webserver is up and running, you can access the homepage by opening a browser and navigating to 
`https://localhost:5000`.  Since this server is running https, a notice will show up that the 
site is not secure.  The user must follow their browser's messages to load the website anyway, and the 
page will load.
