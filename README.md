# Udacity FSND Project 3 
___
This is the third and final project submission for Udacity's FSND Program.  This README will give an outline of the project, the IP address of the web server and a link to the web address with instructions on using the site, a summary of the software installed to run the site, a summary of the server configuration, and a list of any third-party resources used to complete the project.

## Introduction to Project
___
This website is the same website as was submitted in Project 2, deployed to an **AWS Lightsail Cloud Server**, with the following modications made to the website for deployment:
- Modified `applicaiton.py` to `__init__.py` for running as an WSGI app
- Modififed `__init__.py` to run on webserver rather than localhost:
    - Added absolute path to reference the database
    - Removed code from `app.run()` for running the server on port 5000

##### General Overview of Web Page
The website starts at a homepage which will list on the left the different categories in the database, and the list of books in the database in the center. If a user selects a category, the website will return a page that lists the books for that particular category. If a user selcts a book, the webpage will return a page that displays the book title, and an in-depth description of the book. When a user is logged in, buttons for Creating, Updating, or Deleting content will be provided where applicable.

## Accessing the webpage
___
The website is deployed to an __AWS Lightsail Cloud Server__ and can be accessed at this [this link](https://54.234.159.191), or by opening a browser and navigating to `https://54.234.159.191`.  The webpage can also be accessed unsecurely on regular http, however Facebook will require the user to reload the page with https if the user attempts to login.  

## Web App Requirements
___
The following software was installed to run the web application on the server:
- Apache2
- Python 2.7.12
- Python Virtualenv
- Flask
- SQLAlchemy
- HttpLib2
- Python OpenSSL
- mod_wsgi

## Web Server Configuration
___
Due to the HTTPS requirement for Facebook to allow login, the Apache server configuration file also required that a configuration be provided for the server on port 443:
```
<VirtualHost *:80>
		ServerName 54.234.159.191
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/Fullstack_Project3/Fullstack_Project3.wsgi
		<Directory /var/www/Fullstack_Project3/Fullstack_Project3/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/Fullstack_Project3/Fullstack_Project3/static
		<Directory /var/www/Fullstack_Project3/Fullstack_Project3/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


<VirtualHost *:443>
		SSLEngine On
    		SSLCertificateFile /var/www/certKeys/project3.crt
    		SSLCertificateKeyFile /var/www/certKeys/project3.key

                ServerName 54.234.159.191
                ServerAdmin admin@mywebsite.com
                WSGIScriptAlias / /var/www/Fullstack_Project3/Fullstack_Project3.wsgi
                <Directory /var/www/Fullstack_Project3/Fullstack_Project3/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /static /var/www/Fullstack_Project3/Fullstack_Project3/static
                <Directory /var/www/Fullstack_Project3/Fullstack_Project3/static/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
This of course required the generation of self-signed keys to be provided to the server.  For security purposes their location is not listed.  
In order for the server to allow for SSL connections, SSL needed to be turned on, this was dun by running the following command:
```
sudo a2enmod ssl
```
The UFW Firewall was also configured to allow traffic on port 443.
# Third Party Resources
___
No third party resources were used for creating this web page
