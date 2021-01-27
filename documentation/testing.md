# Essential Oils Database Testing

[The Essential Oils Database](http://essential-oils-database.herokuapp.com/get_essentialoils) can be found here.
[The Essential Oils Database Repository](https://github.com/Gwen-of-lynn/EssentialOilsDatabase) can be found here. 
[The Essential Oils Database README](https://github.com/Gwen-of-lynn/EssentialOilsDatabase/blob/master/README.md) can be found here.

---
---
---
## Automated Testing
---
---
### Validation Services
---
The following validation services and linter were used to check the validity of the website code.
- [W3C Markup](https://validator.w3.org/) Validation was used to validate HTML.
- [W3C CSS](https://validator.w3.org/) validation was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.

---
### Python Testing
---
Python was tested by the debugger in app.py. The debugger is currently set to False.

---
---
### Manual Testing
---
---

Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

---
### Testing undertaken
---
All steps on desktop were repeated in browsers: Chrome, Microsoft Edge, and Opera, on large, tablet, and phone screens using the inspect function.

- On all pages:
    - clicked links in nav bar and menu: 
        - Essential Oils, 
        - Home, 
        - New Entry, 
        - Categories, and 
        - sidenav, when applicable.
    -hovered over buttons to check responsiveness
- Essential Oils mainpage:
    - tested search feild,
        - reset
        - search
    - tested the oils fields listed 
        - delete
        - edit
- Edit oils:
    -  - both single and combination
        - 2 different categories
        - with Oil Name and Oil Description empty while others filled in to test if it would allow
- New Entry or Add Oils page:
    - added oils
        - both single and combination
        - 2 different categories
        - with each field empty while others filled in to test if it would allow
- Categories:
    - add category:
        - tested to see if it would allow the category name to be empty
        - added category
    - edit category:
        - tested to see if it would allow the category name to be empty
        - edited
        - canceled
    - hovered over buttons to test colour change
    - tested responsiveness in relation to screensize
        - identified one area for improvement:
            - the cards would look better switched to 2-3 columns at an earlier screensize before it goes to 1 column

    
---
---
## Bugs discovered:

---
---
### Solved bugs

When I first made the edit and add entries/oils pages there was a small dot that was left over from a work around in materialize in the tutorial I used. It would not have been noticible with the original colouring of the panel but once I changed the colour it was there and clickable. It was a drop down categories menu that was used to make the categories a required field that couldn't be skipped. I list it here because of the time it took to figure out how to make it not visable and accessible to users. Eventually I used a .hide class to make the dot invisable. 

Also in my set up I ran into an error that I was having difficulty finding the source of intitially, it was easier to go back a commit and redo the small section where the error was. This unfortunately disconnected me from Heroku and I didn't realize it at the time. That is why there is a gap in activity in the Heroku app.

---
### Unsolved bugs
---
No unsolved bugs at the moment!

There are warnings and 'errors' listed in the gitpod console. These are not actually bugs. The primary source of these is because the parts that are coming up missing are in the base template rather than the individual html files. Another is for the double use of a unique id, however that is in an if/else statement where only 1 will be used. 

---
### Areas for Improvement from manual testing
---
- The cards in Categories would look better switched to 2-3 columns at an earlier screensize before it goes to 1 column
- Slightly increased space between the buttons would look better in Edit Category in mobile size
---
---