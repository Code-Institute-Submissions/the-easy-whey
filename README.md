![Landing Page](/static/readme/landing.PNG)
# Milestone Project 4 - The Easy Whey
# Table of Contents
* [Introduction](https://github.com/KNFullStack/the-easy-whey#introduction)
* [User Experience Design](https://github.com/KNFullStack/the-easy-whey#user-experience-design)  
  * [User Stories](https://github.com/KNFullStack/the-easy-whey#user-stories)
    * [First Time Visitors](https://github.com/KNFullStack/the-easy-whey#first-time-visitors)
    * [Returning Visitors](https://github.com/KNFullStack/the-easy-whey#returning-visitors)
    * [Frequent Users](https://github.com/KNFullStack/the-easy-whey#frequent-visitors)
    * [Admins](https://github.com/KNFullStack/the-easy-whey#admins)
    * [User Story Screenshots](https://github.com/KNFullStack/the-easy-whey#user-story-screenshots)
  * [Structure](https://github.com/KNFullStack/the-easy-whey#structure)
  * [Design](https://github.com/KNFullStack/the-easy-whey#design)
    * [Colors](https://github.com/KNFullStack/the-easy-whey#colors)
    * [Images](https://github.com/KNFullStack/the-easy-whey#images)
    * [Wireframes](https://github.com/KNFullStack/the-easy-whey#wireframes)
    * [Database](https://github.com/KNFullStack/the-easy-whey#database)
    * [Design Deviations](https://github.com/KNFullStack/the-easy-whey#design-deviations)
  * [Limitations](https://github.com/KNFullStack/the-easy-whey#limitations)
* [Features](https://github.com/KNFullStack/the-easy-whey#features)
  * [Current Features](https://github.com/KNFullStack/the-easy-whey#current-features)
  * [Future Features](https://github.com/KNFullStack/the-easy-whey#future-features)
* [Technologies](https://github.com/KNFullStack/the-easy-whey#technologies)
  * [Languages](https://github.com/KNFullStack/the-easy-whey#languages)
  * [Libraries, Frameworks & Programs Used](https://github.com/KNFullStack/the-easy-whey#libraries-frameworks--programs-used)
* [Testing](https://github.com/KNFullStack/the-easy-whey#testing)
  * [Validation](https://github.com/KNFullStack/the-easy-whey#validation)
    * [HTML Validation](https://github.com/KNFullStack/the-easy-whey#html-validation)
    * [CSS Validation](https://github.com/KNFullStack/the-easy-whey#css-validation)
    * [JavaScript Validation](https://github.com/KNFullStack/the-easy-whey#javascript-validation)
    * [Python Validation](https://github.com/KNFullStack/the-easy-whey#python-validation)
  * [User Scenarios - Testing](https://github.com/KNFullStack/the-easy-whey#user-scenarios---testing)
    * [First Time User](https://github.com/KNFullStack/the-easy-whey#first-time-user)
    * [Returning User](https://github.com/KNFullStack/the-easy-whey#returning-user)
    * [Frequent User](https://github.com/KNFullStack/the-easy-whey#frequent-users)
    * [Admins](https://github.com/KNFullStack/the-easy-whey#admin-users)
  * [User Testing](https://github.com/KNFullStack/the-easy-whey#user-testing)
  * [Currently Known Bugs](https://github.com/KNFullStack/the-easy-whey#currently-known-bugs)
  * [Major Bugs Fixed During Development](https://github.com/KNFullStack/the-easy-whey#major-bugs-fixed-during-development)
  * [Lighthouse Results](https://github.com/KNFullStack/the-easy-whey#lighthouse-results)
* [Deployment](https://github.com/KNFullStack/the-easy-whey#deployment)
   * [Project Creation](https://github.com/KNFullStack/the-easy-whey#project-creation)
   * [Publishing](https://github.com/KNFullStack/the-easy-whey#publishing)
   * [Local Clone](https://github.com/KNFullStack/the-easy-whey#local-clone)
* [Acknowledgements](https://github.com/KNFullStack/the-easy-whey#acknowledgements)
  * [Code](https://github.com/KNFullStack/the-easy-whey#code)
  * [Media](https://github.com/KNFullStack/the-easy-whey#media)

You can find the published website here: [The Easy Whey](https://the-easy-whey.herokuapp.com/).
# Introduction

The project is part of a Full Stack Developer course run by CodeInstitute. This is Milestone Project 4. This project was to create a full stack web application with CRUD functionality. This web application is an e-commerce store, where users can create an account, order varying quantities of varying protein powders via a stripe payment system.

## Milestone Project 4

A mockup of the web application can be seen below:

![Mockup Image](/static/readme/mockup.png)

# User Experience Design
## User Stories
### First Time Visitors
* What would I want to see as a first time visitor?
  1. What can I use the web application for, what products can I purchase?
  2. Where can I register?
  3. How can I get in touch with the company?
  4. What ingredients are in the products?
  5. What is the nutritional content of the products?
### Returning Visitors
* What would I want to see as a returning visitor? 
  1. Where can I log in?
  2. How to access my previous orders.
  3. How can I make an order?
### Frequent Visitors
* What would I want to see as a frequent visitor?
  1. Can I save my delivery information?
  2. How can I edit my delivery information?
### Admins
  1. Can I add/edit/delete products/ingredients/nutritional information from within the web application?
  2. How can I check if there have been messages sent from customers?

### User Story Screenshots
Below are screenshots relating to some of the user stories.
> How can I get in touch with the company?
* There is a button that takes a user to the contact page, where a contact form is rendered, where snet messages are accessible to superusers/admins.<br>
![User-Story-1](/static/readme/contact.PNG)

> What ingredients are in the products?
> What is the nutritional content of the products?
* There is a button that takes a user to the product details page, where the product flavours, nutrition and ingredients are shown.<br>
![User-Story-2](/static/readme/nutrition.PNG)

> How to access my previous orders.
* In the accounts menu there is a button for Profile, which shows a user their delivery address (if entered already) along with successful and unsuccessful orders.<br>
![User-Story-3](/static/readme/profile.PNG)

> Can I save my delivery information?
* In the order form first page a user can click the checkbox to save their delivery information or in their profile.<br>
![User-Story-4](/static/readme/savedelivery.PNG)

## Structure
Shown below are elements that correspond to the User Stories:
* What can I use the web application for, what products can I purchase?
* What ingredients are in the products?
* What is the nutritional content of the products?
> Home page contains information about the product, as well as a Products button that shows more detail.
* Where can I register?
* Where can I log in?
> There is a Accounts menu button which shows links for the user to Log in or Sign up. Also trying to access the order form without being logged in will redirect users to Log In or Sign Up.
* How can I get in touch with the company?
> There is a Contact button in the navigation where users can submit questions/queries etc.
* How to access my previous orders.
* Can I save my delivery information?
* How can I edit my delivery information?
> In the order form a user can save their delivery information, or edit it in their profile, and within their profile they can see previous orders.
* How can I make an order?
> There is a button at the bottom of the homepage which takes the user to the order form, or by clicking the Order button in the navigation.
* Can I add/edit/delete products/ingredients/nutritional information from within the web application?
* How can I check if there have been messages sent from customers?
> There are additional navigation items in the Accounts drop down for users marked with Staff status. The options take the superuser/admin to the relevant pages for messages or product alterations.

## Design
### Colors
The main colors throughout are white backgrounds, using coral colour that stands out for buttons.
### Images
The images used throughout are thanks to [Open Doodles](https://www.opendoodles.com/).
### Wireframes
Wireframes images can be seen below and a PDF can be found in the "/static/readme" folder. It contains designs for the desktop and mobile version of some pages. See below for homepage:

* Mobile: <br> ![Mobile Wireframe](/static/readme/XXX.png)
* Desktop: <br> ![Desktop Wireframe](/static/readme/XXX.png)

See link for PDF below:
* [Wireframe](/static/readme/XXX.pdf)

### Database
The database is a POSTGRES database hosted with Heroku, the following models were created within Django:
1. contact app:
    > Contact
2. products app:
    > Product
    > Nutrition
    > Ingredient
3. profiles app:
    > UserProfile
4. subscription app:
    > Order
    > OrderLineItem

See image below for the Entity Relationship Diagram: <br>
[Entity Relationship Diagram](static/readme/entity.png)

### Design Deviations
Compared to the original Wireframe there have been multiple deviations.
* original XXX
> CHANGE XXX
* sub based XXX
> order based XXX

## Limitations
Currently, there some limitations:

* LIMITATION 1 XXX
* LIMITATION 2 XXX

# Features
## Current Features
* FEATURE 1 XXX
* FEATURE 2 XXX
* FEATURE 3 XXX

## Future Features
Features that could be released in subsequent versions include:
* FUTURE FEATURE 1 XXX
* FUTURE FEATURE 2 XXX
* FUTURE FEATURE 3 XXX

# Technologies
Technologies used are as follows.
## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * Used as the main language to code the web applications content.
* [CSS3](https://en.wikipedia.org/wiki/CSS)
  * Used to incorporate custom styling into the web application and its layout.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * Used to create interactive elements.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * Used to create the back end of the web application.

## Libraries, Frameworks & Programs Used
* [Bootstrap 5](https://getbootstrap.com/)
   * Multiple features of Bootstrap 5 were used to create the website. Including grid system, responsiveness and the navbar.
* [Balsamiq](https://balsamiq.com/)
   * Used to create the wireframes when starting the design.
* [Font Awesome](https://fontawesome.com/)
   * Used for multiple icons throughout the web application.
* [Techsini](http://techsini.com/multi-mockup/index.php)
   * Used to generate the mockup image in this README file, see above.
* [GitHub](https://github.com/)
   * Used as a storage location for the website's content, including code and assets.
* [GitPod](https://www.gitpod.io/)
   * An online IDE used to write and test code that is written.
* [Git](https://git-scm.com/)
   * Used for version control to add, commit, and push files to GitHub.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
   * Used to test different CSS styles in the browser, inspect pages, general debugging, confirming JavaScript functionality with the Console and using Lighthouse.
* [favicon.cc](https://www.favicon.cc/)
    * Used to create the favicon.ico.
* [W3C HTML Validator](https://validator.w3.org/)
    * Used to validate the HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * Used to validate the CSS code.
* [JSHint](https://jshint.com/)
    * Used to validate the JavaScript code.
* [Python Validator](http://pep8online.com/)
    * Used to validate the Python code.
* [Postgres](https://www.mongodb.com/)
    * Used as the cloud database provider.
* [Heroku](https://www.heroku.com/)
    * Used as the cloud web application host.
* [AWS](https://aws.amazon.com/)
    * Used to host the static files that the project uses.
* [Django](https://www.djangoproject.com/)
  * Used as the backend framework in which the project was created.
* [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline)
  * Used to generate the entity relationship diagram.

# Testing
Django Unit Tests:
xxx
xxx
xxx

Manual High level testing plan:
1. CRUD functionality in various places within the web application
  > Admin panels, user creating orders, users updating their delivery detail etc.
2. Responsiveness from 320px to 3000px, on multiple browsers:
  > Google Chrome, Mozilla Firefox & Opera
3. All buttons working as intended.
4. No content areas overlapping other content areas.
5. Attempts to force errors with HTML forms.

Test Results can be found here: [Test Results](/static/readme/test-result.xlsx)

## Validation
### HTML Validation
The rendered HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/), via the "Validate by URI" or "Validate by Direct Input" methods.
* TEMPLATE NAME THAT HAD ERRORS XXX
  > XXXX WHAT WAS THE ERROR AND HOW DID I FIX XXX
* WAS THERE A COMMON WARNING?
  > what was common warning and how did I fix? XXX

### CSS Validation
CSS Stylesheet was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), via the direct input method.
* No warnings or errors.

### JavaScript Validation
JavaScript file was run through the [JSHint](https://jshint.com/).
* cusotmfile xxx??
> ERRORS? XXX

### Python Validation
Python files were run through the [pep8online](http://pep8online.com/).
* Warnings were found regarding line length, white spaces around assignment operators and spaces in empty lines.
> These were all corrected and no errors now show.

## User Scenarios - Testing
How does the web application design enable the goals of a first time, returning OR frequent user and admins?<br>
### First Time User
1. GOAL xxx
  * WHAT I DID TO TEST xxx

### Returning User
1. GOAL xxx
  * WHAT I DID xxx

### Frequent Users
1. GOAL xxx
  * WHAT I DID xxx

### Admin Users
1. GOAL xxx
  * WHAT I DID xxx

## User Testing
A user kindly volunteered to test the web application once overall development was complete.
User's comments were as follows:
* COMMENT xxx
  * how to address it xxx 

## Currently Known Bugs
1. None currently known. xxx

## Major Bugs Fixed During Development
1. BUG
> FIX

## Lighthouse Results
Images below show the Lighthouse results on both mobile and desktop:
1. Mobile:<br>![Mobile Lighthouse](/static/readme/XXX.PNG)
1. Desktop:<br>![Desktop Lighthouse](/static/readme/XXX.PNG)

# Deployment
## Project Creation
To create the project, firstly a Chrome extension called "[Gitpod - Always ready to code](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki?hl=en-GB)" was installed. A CodeInstitute template was use by navigating to the [GitHub Repo](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the "Use this template" button. The repository was named "the-easy-whey", the checkbox for "Include all branches" was checked and the green "Create repository from template" button was then clicked. From here, the green "GitPod" was then clicked (must use the above extension) and project folders and files created.

Common Git commands were used as follows:
* git add "filename-here" - used to stage files before commiting them.
* git add . - used to stage all files before commiting them.
* git commit -m "message here" - used to commit changes to the local repositry, with the message containing information on the changes that have occured.
* git status - used to check the tracking status of the file in the project.
* git push - used to push the changes to the GitHub repository.

## Publishing
The project was published using [Heroku](https://www.heroku.com/), the following steps were performed:
1. A requirements file and a Procfile was created within [GitPod](https://www.gitpod.io/) and saved.
  > Requirements file created with: `pip3 freeze –local > requirements.txt`<br>
  > Procfile created with: `echo web: python app.py > Procfile`
2. A new app was created on Heroku, where a name was selected with Europe selected as the region.
3. Within this new app on Heroku, navigate to the "Deploy" tab. Under "Deployment method" click on the "GitHub" icon. From here your GitHub account and Heroku can be linked. Search for the relevent repository name in GitHub in the search area that appears. 
4. Environment variables are saved within a hidden file, meaning that Heroku does not have access to them. Under "Settings", click on "Reveal Config Vars". Various important ket-value pairs are placed here.
5. Navigate back to the "Deploy" branch and click "Enable Automatic Deployment". Heroku will now start to gather data from the assocaited GitHub repository. Future `git push` commands in GitPod will save the data to GitHub and to Heroku, where a live version of the project can be found.

## AWS
CONTENT HERE # XXX CHANGE

## Local Clone
To create a local clone of the project you can follow the steps below:
1. Navigate to the project's [Github page](https://github.com/KNFullStack/the-easy-whey).
2. Click the "Code" dropdown button.
3. From here there are two options:
     * Option 1: Click the "Download ZIP" button to download the files. This can be unzipped locally and opened with your preferred IDE.
     * Option 2: Copy the link from the HTTPS box shown. Then open your preferred IDE of choice and in the terminal window of your preferred directory, use the command "git clone" followed by the link that was copied. For example "git clone https://github.com/KNFullStack/the-easy-whey.git". This will clone the files in the selected directory.
# Acknowledgements
* I would like to say thank you to my mentor Spencer Barriball for his help and guidance throughout the project and the entire course!
* Nutritional information for flavours was taken from [Myprotein](https://www.myprotein.com/).
* Protein descriptions and content taken from [The Protein Works](https://www.theproteinworks.com/).

## Code
* Thank you to stackoverflow user [Adam Nelson](https://stackoverflow.com/users/26235/adam-nelson) for the help with differentiating between multiple forms in a single view [here](https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django).
* The login and register functionality was adapted from lessons contained with the [Code Institute](https://codeinstitute.net/) course, using the [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).
* Thank you to [Goran Štimac](https://www.goranstimac.com/) for their help with Bootstrap Toasts, link to the post can be found [here](https://www.goranstimac.com/blog/how-to-add-bootstrap-5-toast-on-page-load/).
* Thank you to [Görkem Arslan](https://garslan.medium.com/) for help with customising the 404 page, link to the post can be found [here](https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317).

## Media
* The images used throughout are thanks to [Open Doodles](https://www.opendoodles.com/).
* Thank you to Andrew Paglinawan and [Kimberly Geswein](https://www.kimberlygeswein.com/) for their fonts: [Quicksand](https://fonts.google.com/?query=Andrew+Paglinawan) and [Shadows Into Light](https://fonts.google.com/specimen/Shadows+Into+Light?query=Kimberly+Geswein), respectively.