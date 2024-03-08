# Introduction

This is my project for E-commerce and it has ben creaded in Django! For this project i decided to do an online store that sells items for babies from 0-12. This store sells clothing and tableware for weaning babies onto solid food.The name of my store is called Baby Things!.
There is an admin panel for Admin users the log in information for this will be found at the end of this ReadMe. Please scroll to the bottom of this page and you will see a heading for log information and first you wil see my git sign in informatuon and under that you will see the admin panel log in informatio.

The data base for my blog is hosted on [elephantsql](https://www.elephantsql.com/) 
The site will be deployed threw [Hreoku](https://id.heroku.com/)
Images stored on [cloudinary](https://cloudinary.com)

# How to begin
 When you first arrive on my website you will be on the home page. This page had a background image and a button saying shop now that will take you to the Products home page.On the home page of the store you will find a " nav-bar " at the top of the page with 4 links. These links are connected to different pages. The first link is All clothing where you can discover items for sale via links of - Price,Catagory and All Products. The second link is called Clothing and this has many options to select for example "boys 0-6, sleepsuits, and All Clothing", thirdly there is a link in the nav bar for Dinner things this is the link for cutlery plates and bowls and bibs. Finally we have the last link in the nav bar and this is the "Special offers" link. This will lead you to deals and new arrivals. Above the nav bar there is a search bar that you can type in to search the site this link withh accept key words in the description of the items as well as category names. To the right of that you will find a "My Account button this will allow you to either sign in or login and beside that again you have the shopping bag. The shopping bag will be updated as you add to bag and you can see the price and increment or decrement the quantity as needed." You are able to sign up as a registered user with a user name and an email confirmation will be sent to your email address you provided and you will need to verify this. This will also be send to the console on the ide of your choice for viewing the code from git.

# Shopping bag functionality:
When you click on the shopping bag you are brought to a seperate page. (*note in future versions i intendend to have this shopping bag as a pop up overlay on your current page so you are not redirected and it is easier to continue shopping.)
So on this seperate page you will see alist of items you have purchased and the price of the item you can select a quantity for purchase. As you incremnet this function the total of your shoppinh bag will increase. You can also decrement your quantity and this will remove items from your cart and in turn the price will decrease. Then you will notice that there is a delivery fee that is calculated depending on the total in your cart.

## Templates

In the directories base.html is the main template and my other templates inherit from that 
Index.html is the form that handles displaying my products. I have copied templates from a "<p>" and your not register for class or id. I have an sign-up form that enables users to sign up and this is linked to my email model so that in the admin oanel my cutomers emails are automatically added to my system. In futur versions i intend to work on this and add more information and have more details added to my admin panel.

## Authorisaton

djnago framworks have the ability to implement an admin feature on the backend, from here i can create read update and delete products and customer profiles fro my store . I have 5 models linked and they are Categories, Customers, Deliverys, Order_History and Products. I can also create a user name and password from this admin site. I can verify email address. On the admin panel there are roles and permissions. The abilty to create an admin and this person has the abily to preform all parts of crud on the site for each model. 

## Login and Registration

Threw Django i implemented login/logout abiliies and the ability to register as a user for the site.  you are able to create a passowrd to log in. You are able to change your password aswell if you have fogotten it.

## Database management

In order to create models and store recipes and blog posts i used [elephantsql](https://www.elephantsql.com/). When creating updateing or deleting parts of the models you make migrations threw the terminal window and this will update the database on elephantsql. 

## CRUD

By logging into the admin panel The super user has the ability to preform full crud functionality my creating posts deleting them, updating usernames and passwords. 

## Images
My images are hosted on elephantsql

## Testing

* I will be manually testing my Baby Things Store for this Project!

* To begin with i started testing the the Main page I began with the buttons! i tested each navigation button first by hoovering my mouse over it to see would my hopover function correctly work which i found it did! I then clicked each
navigation button to be sure the links i created for the button would bring me to the correct page. They did. 
after that i went to each nav button on all my pages to see would the link continuously work as intended! I tested Each nav button for a drop down bos which was succesful i then manually clocked each button to ensure that i was brought to the correct page i intend for suers to go to. In the beginning of the project i noticed that if i was logged out of the admin panel then i was unable to access the store entirely. In the end it was a spelling error of the top pagenav header,html page for the accounts.signup link, once i corrected this there was no issues for signing in and out of the store either logged in or out from the admin panel.


* Next i moved on to the blog page. I clicked into my first blog** as if i were a user I ecpected this to bring me into a page with the contect of the blog i clicked the reuslt was as intended and i was indeed brought to the content i was expecting to see. I then went to my like function to click that to see would it work and it did then i moved down to the comment section i left a comment as my logged in user which i then went to the admin page and approved the comment and when i returned to the blog post my comment was there!

I did the same on my recipe model was able to leave a comment. When i creatred the seperate page for recipes i uploaded a blog post to the site and made sure that it only posted to the recipe page and it did.

* To test the log in feature i created a sudonom and logged into the site as sarah she was ablel to register and create a passwprd i then went and tried to change her password and was successful

* To comment on the site i used sarahs accound and left a comment iI then logged in as my admin user and approved the comment. Initially the option to approve wasnt there and i had made an error with my comment model i went back and changed the model and then was able to approve sarahs comment 
![sarah](images/sarah.png)

# bugs

I wanted to implement the ability to edit and delete comments the user had made on the blogposts and recipes but after impletmenting the code from the [django documentation](https://docs.djangoproject.com/en/5.0/) but i could not get this to work for me just yet i will contu=inue in my efforts to perfect this.

# Validator Testing

## Tested on [Validator](https://pep8ci.herokuapp.com/)
Code passed through validator with no issues
![val](images/val.png)
![val1](images/val1.png)
![val2](images/val2.png)
![val3](images/val3.png)
![val4](images/val4.png)


# Credits 
I took ideas for this project from the code institute walkthrough project Ado. 

# Important links
Link to my GitHup repository

# log in information

GIT log in: Stephaniemaf
passoword: AvaAlex1@

To get onto admin site 
Name: admin
Password: project5


hosted on heroku