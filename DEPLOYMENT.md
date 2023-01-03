# Deployment instructions for the project


- The program was deployed to [Heroku](https://dashboard.heroku.com) initially then moved to [Render](https://render.com/).
- The program can be reached by the [link](https://issue-tracker-mnl3.onrender.com/)
### Local deployment:

*Note:*
  - This project requires install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/IuliiaKonovalova/issue_tracker).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/issue_tracker.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/IuliiaKonovalova/issue_tracker)

---

1. Create a .gitignore file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a .env file. This will contain the following environment variables:

    ```python
    import os

      os.environ("SECRET_KEY", "Add a secret key")
      os.environ("DATABASE_URL", "will be used to connect to the database")
    ```

1. Run following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.

---

**The app was initially deployed to Heroku then moved to Render since Heroku has removed its free tier services from November 29 2022**

---


### Heroku Deployment

1. Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type in this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
1. Go to [www.heroku.com](www.heroku.com) 
1. Login or create a Heroku account.
1. Create a new app with any unique name <name app>.
1. Create a Procfile in your local workplace, which will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.

1. Go to resources in Heroku and search for postgresql. Select Hobby dev - Free and click on the provision button to add it to the project.

1. Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars and add the following config variables:

| Key      | Value          |
|-------------|-------------|
| DATABASE_URL | ... | 
| DISABLE_COLLECTSTATIC | 1 |
| EMAIL_HOST_PASS | ... |
| EMAIL_HOST_USER | ... |
| HEROKU_HOSTNAME | ... |
| SECRET_KEY | ... |


1. Copy the value of DATABASE_URL and input it into the .env file.
1. Create EMAIL_HOST_PASS and EMAIL_HOST_USER with gmail account and add values to these keys.
1. Migrate changes.
1. Set debug to False in settings.py
1. Commit and push the changes to GitHub.

---


## Render Deployment

### Create Database on ElephantSQL

1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account.

2. Create a new instance of the database.

    - ![ElephantSQL. Create a new instance](documentation/deployment/elephantsql_create_new_instance.png)

3. Select a name for your database and select the free plan.

    - ![ElephantSQL. Select a name for your database](documentation/deployment/elephantsql_name.png)

4. Click "Select Region"

    - ![ElephantSQL. Select a region](documentation/deployment/elephantsql_select_region.png)

5. Select a region close to you.

    - ![ElephantSQL. Select a region](documentation/deployment/elephantsql_select_region_near_you.png)

6. Click "Review"

    - ![ElephantSQL. Review](documentation/deployment/elephantsql_click_review.png)

7. Click "Create Instance"

    - ![ElephantSQL. Create Instance](documentation/deployment/elephantsql_click_create_instance.png)

8. Click on the name of your database to open the dashboard.

    - ![ElephantSQL. Open dashboard](documentation/deployment/elephantsql_click_db_name.png)

9. You will see the dashboard of your database. You will need the URL of your database to connect it to your Django project.

    - ![ElephantSQL. DB](documentation/deployment/elephantsql_db_url.png)