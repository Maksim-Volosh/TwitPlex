# TwitPlex

## Description
TwitPlex is a platform for sharing thoughts, ideas and news. Here you can create and post tweets, share your opinion and be inspired by the content of other users. Keep track of the latest trends, join discussions, make new friends and chat with like-minded people. Join TwitPlex and discover endless opportunities to communicate and share ideas!

## Content
- [Description](#description)
- [Install](#install)
- [Using](#using)

## Install
1. Clone repository:
    ```bash
    git clone https://github.com/Maksim-Volosh/TwitPlex.git
    ```
    And go to repository folder
2. Create environment an activate:
   
   Create environment:
     
    ```bash
    python -m venv .venv
    ```
    
    Activate venv:
      
    ```bash
    .venv\Scripts\activate
    ```
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Create config file:
   
   Create in TwitPlex/ folder `config.py` file.
   In this file write this:
   ```python
    SECRET_KEY = "Enter your secret key"
   ```
5. Create your redis server:
     - Go to [this website](https://redis.io/try-free/), and create an account or login.
     - After registration you will alredy have a redis db, if this not true, create a new redis db.
     - Go to database and copy: Public endpoint, Default user, Default user password and go to `config.py`.
     - Add to your `config.py` this:
       
        ```python
        REDISURL = "Public endpoint"X
        REDISUSERNAME = "Default user"
        REDISPASSWORD = "Default user password"
        ```
6. Create the `superuser`:
   ```bash
   python manage.py createsuperuser
   ```
8. Create google oauth clientid for signin with google for djano application.
   
7. Run server and go to admin panel:

   Run server.
   
   ```bash
   python manage.py runserver
   ```
   Go to admin panel `http://127.0.0.1:8000/admin`:
     - Log in as a previously created user.
       
   Go to `Sites`:
     - And create a new site with domein and name: `http://127.0.0.1:8000/`
       
   Go to `Social applications`:
      - And create a new Social application:
        
        `Provider: Google`
      
        `Name: google`
      
        `Client id: "Your cliend id"`
      
        `Secret key: "Your secret key"`
      
        - In input `Sites` you should be choice your site - `http://127.0.0.1:8000/`
    - Your form should be view this:
  
     ![image](https://github.com/Maksim-Volosh/TwitPlex/assets/114184285/82d0183a-eca3-49ab-8281-6ac4d49f88a6)
   * On this tip we finished the settings
  
     

   #### After this, if you get error `django.contrib.sites.models.Site.DoesNotExist: Site matching query does not exist.`:
     - Go to `settings.py`, find the `SITE_ID` and change the number of this variable to the id of your `Sites`. you can view this id in database.
     - For example i somehow have a id 3:
       
       ![image](https://github.com/Maksim-Volosh/TwitPlex/assets/114184285/cc00199f-a9ca-4e03-a80b-6faa16974dda)

## Using
- Go to terminal and write:
 
  ```bash
  python manage.py runserver
  ```
  I am Grateful, you has successfully installed the app 😍🥳🎉

## Pssss!!!!... Click the star pls......
