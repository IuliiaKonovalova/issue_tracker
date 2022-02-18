# Django issue tracker

---

## About

This [issue tracker](https://issue-tracker-by-konovalovs.herokuapp.com/) was created to help people to create and track issues in their personal or team projects. It is a simple and easy to use issue tracker that allows you to register your account, create projects, issues, add comments, and track the status of your issues.

---

## User stories

### First Time Visitor Goals:

1. As a **First Time Visitor**, I want to **easily understand the main purpose of the app**, so I can **learn more about this app**.

1. As a **First Time Visitor**, I want to **be able to easily navigate through the app**, so I can **find the content**.

1. As a **First Time Visitor**, I want to be able to **register my account**, so I can **learn benefits of the app as a user**.

1. As a **First Time Visitor**, I want to **find the app useful**, so I can **use it according to my needs**.

### Registered User Goals:

1. As a **Registered User**, I want to **be able to log in to my account**, so I can **have a personal account**.

1. As a **Registered User**, I want to **be able easily login and logout**, so I can **access my personal account information**.

1. As a **Registered User**, I want to **be able easily recover my password in case I forget it**, so I can **recover access to my account**.

1. As a **Registered User**, I want to **be able change my password**, so I can **be sure that nobody else can access my account**.


1. As a **Registered User**, I want to **be able to create a personal project**, so I can **keep track of my progress**.

1. As a **Registered User**, I want to **be able to create a team project**, so I can **work on a project along with other developers**.

1. As a **Registered User**, I want to be able **safely work on projects with my team**, so I can **be sure that only my team has access to this project**.

1. As a **Registered User**, I want to **be able to add collaborators to my team project**, so I can **choose with which people I will work with**.

1. As a **Registered User**, I want to **be able to create issues for a project**, so I can **increase productivity of my or team work**.

1. As a **Site User**, I want to be able to **comment on the issue created**, so I can **add some additional Registered on the bug**.

1. As a **Registered User**, I want to **be able to track and change the status or type of an issue, so I can **see the status or type of an issue**.

1. As a **Registered User**, I want to be able to **upvote an issue**, so I can **show that I have the same issue as someone has already posted**.

1. As a **Registered User**, I want to **be able to use an interactive kanban board inside projects**, so I can **easily apply changes to the issues**.

1. As a **Site User**, I want to be able to **comment on the issue created**, so I can **add some additional information on the bug, feature, task, or user story**.

1. As a **Registered User**, I want to **be able to edit or delete my projects, issues, comments, and votes**, so I can **be sure that I can apply any changes t my notes**.

1. As a **Registered User**, I want **to be able to see the list of all projects I created or am a collaborator of**, so I can **understand on which project I should work on**.

1. As a **Registered User**, I want to **be able to see the list of all issues I created or I was assigned to**, so I can **understand on which issue I should track or I have to work on**.

1. As a **Registered User**, I want to **be able to view other users' profiles**, so I can **learn about other users' activity**.

---

## Features

1. Landing page

   - When you visit the site, you will see a landing page with a welcome message and buttons to register or log in.

   ![landing page](documentation/website_screenshots/landing_page.png)

1. Sign up

   - When you click the "Sign up" button, you will be redirected to a sign up page. After filling out the form, you will need to confirm your email address.

   ![sign up page](documentation/website_screenshots/sign_up_form.png)

   - You can register a new account by filling in the form and clicking the "Sign up" button.

1. Log in

   - When you click the "Login" button, you will be redirected to a log in page.

   ![log in page](documentation/website_screenshots/sign_in_form.png)

   - You can log in to your account by filling in the form and clicking the "Sign in" button.

   - If you forgot your password, you can reset it by clicking the "Forgot password?" button. You will be redirected to a page where you can enter your email address and click the "Reset password" button.


1. Projects list

   - After you log in, you will be redirected to the projects list page.

   ![projects list page](documentation/website_screenshots/projects_list.png)

   - You can see a list of all projects you created or are a collaborator of.
   - You can click on a large plus button to create a new project. You will be given a choice of personal or team projects.

   ![create project page](documentation/website_screenshots/create_project_button.png)

1. Create project

   - When you choose the type of project you want to create, you will be redirected to a create project page.

     - Personal project form:

     ![create personal project page](documentation/website_screenshots/create_personal_project.png)

     - Team project form:

     ![create team project page](documentation/website_screenshots/create_team_project.png)

1. Project details

   - After you click on a project, you will be redirected to the project details page. Here you can see all the information about the project and an interactive kanban board to work on the issues. From here you can to go to each collaborator's profile page, create and manage issues, and edit and delete the project if you created it.

   ![project details page](documentation/website_screenshots/project_details.png)

   - You can click on "add issue" to create an issue for the project, you'll be redirected to a create issue page, where you can add a title, description, choose its priority and type, and add assignee.

   ![create issue page](documentation/website_screenshots/create_issue.png)

1. Issue details

   - After you click on an issue, you will be redirected to the issue details page. Here you can see all the information about the issue, including the comments and the status of the issue. From here you can to go to creator's and assignee's profile pages, add and edit comments, and edit and delete the issue if you created it.

   ![issue details page](documentation/website_screenshots/issue_details.png)

1. Profile page

    - You can go to your profile page by clicking on "Profile" in the account menu at the top right corner of the page. Also, you can visit other users' profile pages by clicking on their names in the projects list or issue details pages.
    
    - Here you can see users' information and their statistics.

    ![profile page](documentation/website_screenshots/profile_page.png)

    - If you are on your profile page, you can also see a password change form at the bottom of the page.

    ![password change form](documentation/website_screenshots/password_change_form.png)


---

## Technologies used

- ### Languages:
    
    + Python: the main language used to develop the server side of the website.
    + JavaScript: the main language used to develop the client side of the website.
    + HTML: the markup language used to create the website.
    + CSS: the styling language used to style the website.

- ### Frameworks and libraries:

    + Django: python framework used to create all the logic.
    + jQuery: javascript library used for creating interactive elements, such as the kanban board, and to send AJAX requests to the server.

- ### Databases:

    + PostgreSQL: the database used to store all the data.

- ### Other tools:

    + Git: the version control system used to manage the code.
    + Heroku: the hosting service used to host the website.
    + Github: used to host the source code of the website.
    + Visual Studio Code: the IDE used to develop the website.
    + Chrome: the browser used to view the website.

---




## Wireframes

### Home page

![Home Page. Desktop Screen](documentation/wireframes/home_page.png)

### Login page

![Login Page. Desktop Screen](documentation/wireframes/login_page.png)

### Register page

![Register Page. Desktop Screen](documentation/wireframes/register_page.png)

### Profile page

![Profile Page. Desktop Screen](documentation/wireframes/profile_page.png)

### Projects page

![Projects Page. Desktop Screen](documentation/wireframes/projects_page.png)

### Project page

![Project Page. Desktop Screen](documentation/wireframes/project_page.png)

### Issue page

![Issue Page. Desktop Screen](documentation/wireframes/issue_page.png)
