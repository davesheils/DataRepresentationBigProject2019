# DataRepresentationBigProject2019

This is my Data Representation Web Application Project submitted as the "Big Project" part of the assessment for the Data Representation module in the Higher Diploma in Data Analytics programme (Autumn 2019 semester). There are a small number of loose ends that could be tied up, and may be so in the coming days. However, I understand that any updates committed after midnight 24th December 2019 will not be considered for marking.

## Aims of the project:
The original plan was to create a simulation of an online shop selling music, books, games etc. This explains why it is designed to connect to a database called "shop", and a main table called "stock" and why there are fields relating to Quantity and Price. The idea was that the customer could view the items in a data table and then be able to view further information about the product, data that would be pulled variously from the discogs, goodreads, imdb (if the item were a dvd) and/or wikipedia. I presume there is a similar resource for games. The final version is confined to music items only. The final version is confined to data relating to CDs and Vinyl LPs only.

## Core Functionality.

The modules in this project are:
CreateAndPopulateStockDataBase.py
This is run once to populate a mysql database with items listed in a csv ('stock.csv')

## StockDAO.py
The Data Access Object file, modelled closely on the BookDAO file from the lectures

## application.py
This is the rest server. It is so titled for online deployment.
In addition to the CRUD functions, this server contains:

methods to render the various web pages associated with the project (see templates folder):
* home
* login
* logout
* moreinfo

There is also a method (sign-in) to validate the login credentials of the user.

You can login using the following details:
* username: admin
* password: pass1

or either of the other two logins that you will find in the users dictionary defined in the code

## Data Table and CRUD functionality:
On successful login, you will be able to view a list of LPs/CDs. You can add, delete or update one of these items (note: if the added/updates do not appear in the list, click jome to refresh). If adding a new item, it would be helpful to add teh correct discogs id, but the add/update function should work regardless.

## More Info page and functionality
The User can get more info about the recording by clicking the more info button. This takes a couple of seconds to complete (a "please wait" message to the user would have been helpful here). When the page loads, the user is given summary info (title, Artist(s), Genre(s) of the recording, as well as the tracklisting. This funcitonality is enabled using the official python client for the discogs API. The user also gets a summary paragraph about the recording from the relevant page from wikipedia (from the python wikipedia API client).

## Online implementation:

The application is hosted online at davidsheils.pythonanywhere.com. There were issues with connecting to the backend data base which were not conclusively resolved as of 20.28 on the 24/12/2019. Therefore, functionality dependendent on the backend database may not work online. The moreinfo function should work by going to davidsheils.pythonanywhere.com/moreinfo/id where id is any valid discogs id.

## Templates and serverside webpage rendering.
This project makes limited use of flask templates to dynamically insert content into pages (e.g you are logged in as ...) and the content onthe more info page. I only discovered this functionality late in the development process, and, although the topic was outside the scope of the course, I would have liked to explore this feature more.

## Loose ends
The item id should be hidden from the user during create and update.
Form validation was in place in earlier versions of the project. This was removed to simplify the code to concentrate on developing the core functionality of the project. However, the potential for extra marks has almost certainly been sacrificed here.

The online database connection issue was not resolved and valuable time was lost on this given that only a small amount of marks were available for it.
