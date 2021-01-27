# Essential Oil Database
---
---
---
This site is a database where users can store, and share, knowledge of essential oils, their uses, and different ways to combine them. This site is not intended to take the place of any medical advice.

Oils are searchable as well as displayed in a collapsible accordian in the main page. Each oil is displayed with name, whether it's a single oil or a combination of oils, a description, and a marker of whether the source of the information is included to help aid other users in their own research.

---
---
## UX
---
---
### Project Goals
---

The Essential Oils Database aims to provide an easily searchable, open-collaborative database to allow users to share their knowlegde and ideas for innovative combinations.

Again, the information shared is in no way aimed at taking the place of medical advice and users are expected to do their own research.

---
#### Target Audience
---

The target audience for The Essential Oil Database are users of essential oils, and small businesses selling essential oils.

---
##### User Goals are:
        
- Easily findable information
- Ability to share knowledge and experiences
- New oil combinations they may not have thought of before
- Database and webpage laid out in an intuitive way
 
##### The Essential Oils Database is a great way to meet the needs of Essential Oil users because:

- It is an open collaborative database 
- Users can easily add their own knowledge and experience with oils and add to the information available-- It has an easy and intuitive layout
- Way to find small buissnesses selling essential oils

---
	
##### Small Business Goals
- Potential to give this database to clients
- Easily findable information
- Database and webpage laid out in an intuitive way
- Expanding customer base
- Advirtising opertunities 

##### The Essential Oils Database is a great way to meet the needs of Essential Oil Small Businesses because:

- Provides a reference catalogue for both the business and their potential clients
- Easy to spot and correct misinformation as well as finding out common misconceptions of potential clients
- New oil combinations they may not have thought of before
- Ability to reference their own page and low key advirtise
- Potential for a new market

---

##### Developer Goals:

- This database provides a great opportunity to gain experience in new and familiar languages
- Expand the developer’s portfolio.
- Combine an interest in essential oils with a professional interest in webpage dev and des.
 
---
#### User Stories

##### As an essential oil user, I want:

- Accurate, easy to interpret information in an easy to use system
- The ability to share my knowledge with others
- A way to view and try other success stories

---

##### As an essential oil small business owner, I want:

- A way to provide my clients with well sourced information in an easily accessible, attractive webpage or app.
- A way to expand my client base
- A way to encourage purchases
- Client suggestions on oils and oil combinations that have worked for them to expand my inventory.
---
---
### Design Choices
---
---
#### Fonts

For my fonts, I kept the standard materialize fonts and the default sizes for HTML as I found they work well for the site.

In future I would like to include fonts, or the option to switch to fonts, with a mind to accessibility. Fonts designed with users that may have difficulty reading for various reasons that do better with specific fonts.

#### Icons

The icons used were the Font Awesome icons suggested by the Code Institute's tutorial for a database site, I found they fit with the Essential Oil database as well so I kept with that. Except for the checkmark for the source included, as I feel the checkmark fits that better than the icons referenced in the tutorial. 

        "Source included?" 

        "Check!"

 
#### Styling

For the colours used I started with an idea of wanting an off white colour for the main text and a dark background colour. The panels with the lighter backgrounds and the darker text use the same colour as the background. The darker background area and lighter text use the off white colour, including for the Font Awesome icons. The buttons and the navbar also match in colour. I used the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel) to find most of the colours and how they combined. I also used Materialize and Font Awesome for styling. 

In future I would like this site to have options in colour schemes, and fonts, to increase accessibility.

The containers, nav, and menu were all similar to the tutorial used to put the project together, mostly because it works very well for this project as well. 

---
---
 ### Wireframes
 ---
 ---
 
 
The wireframes were created using [Balsamiq](https://balsamiq.com/) while planning this project. While the project has changed slightly since the wireframes were made the core styling remained. 

[Minimal Viable Product Wireframe](https://github.com/Gwen-of-lynn/EssentialOilsDatabase/blob/master/documentation/Essential%20Oil%20MVP.pdf)
[Future Site Wirefram](https://github.com/Gwen-of-lynn/EssentialOilsDatabase/blob/master/documentation/Essential%20Oil%20WF.pdf)
 
---
---

## Features
---
---

### Current Features
---
#### 1. Search Panel
Friendly, easily usable, search panel that can be used to search for keywords from the description or the oil name. 

#### 2. Collapsible List of Oils

The collapsible list of oils on the main page provides the information for each oil in a standard, easy to read, format.

#### 3. Navbar and Sidenav

The top navigation bar and the side navigation, for smaller screens, allows for easy, convienent, and intuitive navigation for all screensizes. 

#### 4. CRUD for Oils and Categories (but never in the diffuser)

This site allows for users to create, retrieve, update and delete data from the database on Mongodb.

---
### Features Left to Implement
---
In future I would like this site to have:

- styling options with accessibility in mind.

- other accessibility options, such as text to voice.

- search function to work for categories and not just essential oil name and description.

- sign in, so that not signed in users can search while signed in users would be able to create, edit, and delete depending on their level of authorization. Images for categories, background, and side nav. Potentially able to be chosen by users when they add oils and categories.
    
- oils marked as new, or verified, by an admin. 
    
- a random oil picker and potentially a match game for oils and their main property.
    
- flash messages shown as pop up modles
    
- defensive modle prompts asking if people are sure of changes made, including deletion
    
- sorting by single oil or combination.
    
- radio buttons for adding multiple searchable tags
    
- adding search capbilities by "and", not just "or"
    
- drop down options from the navigation bar
    
- tabs across the top of the accordian collapsible list of oils with the names of categories so that only that category will be shown in the collapsible.
    
- section to add recipes and recommendations for homemade essential oil products. For example: lotions, lipbalm, and room sprays.

---
---
## Technologies Used
---
---

#### Tools:

-[Balsalmiq](https://balsamiq.com/) to make the wireframes
-[PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project
-[MongoDB](https://www.mongodb.com/cloud/atlas) for the database for this project
-[GitHub](https://github.com/) to store and share all project code remotely
-[Gitpod](https://www.gitpod.io/) to compile and create code
-[Dillinger](https://dillinger.io/0) to make this readme file

#### Libraries

[JQuery] (https://jquery.com/) to simplify DOM manipulation
[Materialize] (https://materializecss.com/) to simplify the structure of the website and make the website responsive easily
[FontAwesome] (https://www.bootstrapcdn.com/fontawesome/) to provide icons for The Essential Oil Database
[PyMongo] (https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible
[Flask] (https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages
[Jinja] (http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html
[Heroku](https://dashboard.heroku.com/apps) to build, run, and operate applications entirely in the cloud. To allow Flask, Python, Jinja, Github to work together.

#### Languages

This project uses HTML, CSS, JavaScript and Python programming languages.

---
---
## Testing
---
---

Testing information can be found in separate [testing.md](https://github.com/Gwen-of-lynn/EssentialOilsDatabase/blob/master/documentation/testing.md) file.

---
---
## Deployment
---
---
I deployed this page from Github to Heroku. Heroku has already made a video on how to do this, which I have linked below.

[Heroku Deployment Methods] (https://www.youtube.com/watch?v=fW3yWiRd4E4)

---
---
## Credits and Acknolodgements
---
---

For this project I followed a tutorial from Code Institute for a Task Manager Database and adapted for my own database, styling and project needs. 

For the error pages I used and adaped code from [this custom error pages site] (https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

The structure of this readme is based on [A Greave’s Picflip and Familyhub readme files] (https://github.com/AJGreaves).
 
##### Special thanks to:
Aaron Sinnott, my mentor for this milestone project.

-Structure of this readme is based on Anna Greave’s picflip and familyhub readme file.

### Disclaimer

The content of this website, including the images used, are for educational purposes only. None of the content of this website should be used to take the place of medical advice.
 
