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

I will be manually testing my Baby Things Store for this Project!

## Home Page
 ### Navbar: <br>
 I tested each navigation button first by hoovering my mouse over it to see would my hoover function correctly work which i found it did! I then clicked each navigation button to be sure the links i created for the button would trigger a drop down menu <br>
 I clicked on All Things. This immediatly threw an error at me. If i was logged out of the admin panel then i was unable to access the store entirely. The error was showing the pagenav.html as causing the error. I went threw the code and noticed it was a spelling error at the top pagenav header html page for the accounts.signup link, once i corrected this there was no issues for signing in and out of the store either logged in or out from the admin panel. I went back to the home page and tried the All Things link again This dropped a menu down containing all expected options for product pages.<br>
 I clicked on Clothing Things Things. This dropped a menu down containing all expected options for product pages.<br>
 I clicked on Dinner Things. This dropped a menu down containing all expected options for product pages.<br>
 I clicked on Specials Offers. This dropped a menu down containing all expected options for product pages.<br>
 I clicked on My Account. This dropped a menu down containing all expected options.<br>
 I clicked on the Shopping bag. This brought me to a knew page with the options to go back or continue to checkout. As i had no items in my bag to view thats all that was on the page and what i expected to see.<br>
 I clicked on the Search bar. I wanted to be able to type in this bar and have it find the product im looking for via product name or part there of, or via item heading. it did work and i was brought to the item page i was searching for<br>
 ### Middle Container
 The container has a background image with text overlay. This is centered and stretched to fit the whole screen but have padding at the edges.
I clicked on the shop noew button contained on this page and under the text informing customers of New Arrivals. This brought me to a new page with all the lasted items added to the store contained in it. This test passed like i expected.

### The Footer:
Expectation = I expect the footer to have the words Made by stephanie and links to facebook and instagram. I want these links to lead to the home page of their respective sites.
Result = I clicked on each link and am brought to the front page of their respective sites.

### Shopping Bag
Expectation: I expected this to bring me into a page with the content of the shopping bag. sign up form i clicked  theon the bag and was shown an attribute error saying that reuslt was as intended and i was indeed brought to the content i was expecting to see. 

# Product Testing

## View Product
Expectation: I will click on a Sleepbags in the Clothing things drop down menu to test this feature. I expected to be brought to the Sleeping bag item page. <br>
I was brought To the oage with the image i had chosen to represent my sleepbags
Fix: No fix needed as i was indeed brought to the correct page. I was shown the product image of a sleep bag and i had the option to add it to my cart or keep shopping.

## Add Product
Expectation: I will be logged in as admin and i will select the My Account option on the nav bar. I will be shown a menu item called Product management. Here a form will be present and i will be able to fill in the fields with my new image. To test this i chose to ass a silicone bowl to my site. I filled in all the required fields and clicked on the add button. To text if this worked i clicked on the search bar above and typed the word Silicone. This then brought me to a product page with the item image of a silicone bowl with the clearnce tag i chose to save it under and it had a price that i chose aswell.
Fix: This test was successful

## Edit Product
Expectation: I will select the newly added silicone bowl and i will edit the price to 1.99
Fix:


## Delete Product
Expectation: I will again use the silicone bowl and i will click on the delete button i created and i expect the product to be deleted from my site.
Fix:

## Facebook business page
[Facbook](https://www.facebook.com/profile.php?id=61557082624595)
![fbbus](static/images/fbbus.png)
![fbbus1](static/images/fbbus1.png)

# Validator Testing

## Tested on [Validator](https://pep8ci.herokuapp.com/)
Code passed through validator with no issues
![val](static/images/.png)
![val1](static/images/val1.png)
![val2](static/images/val2.png)

# bugs

I wanted to implement the ability to edit and delete comments the user had made on the blogposts and recipes but after impletmenting the code from the [django documentation](https://docs.djangoproject.com/en/5.0/) but i could not get this to work for me just yet i will contu=inue in my efforts to perfect this.


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