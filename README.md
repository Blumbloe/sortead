# sortead

Sortead is designed to deliver an informative and practical experience allowing users to not only learn about the restaurant but also allow them to book a table.

The site is aimed to target people who are interested in the restaurant and those who want to make a reservation.

[The site can be viewed here.](https://blumbloe.github.io/sortead/)

## 1. User Experience
The website is created on the behalf of the service provider. The aim is to allow the user to book a reservation for their party on a specific time and date.

The site provides the ability to book a table, along with the ability to read about the restaurant and check out the menu. 

### User Goals
- Online Booking
- Menu
- Cancellations
- About section
- review section

### User Stories
- As a site owner I can take online bookings for the eatery so that customers can easily book a table.
- As a User I can view the menu online so that I can decide what I will order beforehand.
- As a User I can cancel my booking so that if circumstances change the timeslot wont be wasted.
- As a User I can book multiple guests for a meal so that the restaurant can prepare for our party appropriately.
- As a User I can leave a review online so that I can let other potential customers know how great the food and service was.
### Target Audience
- Site Owner
- Potential Customer
- First-Time Visitor

I have employed the use of the projects function on my repository to keep track of the user stories so that the user stories are recorded along with the task and acceptance criteria required to meet the goal.

![Project card from github](/sorteadproject/static/documentation/user-story-1.png)

Additionally, each goal has been put in order of importance. There are must haves, should haves and could haves. This enables me to discern which targets I need to work on first so that I can meet the minimum functionality of the site.

![Project Board from github](/sorteadproject//static/documentation/project-board.png)

## 2. Design
### 2.1 Colour Scheme
For my colour palette I used [coolors.co](https://coolors.co/) to create the colour palette that matches my vision for the site. I wanted to keep it mostly neutral while having the important elements such as the buttons stand out.

![Colour palette with hex colour codes and colour names](/sorteadproject/static/documentation/colour-pallete.png)

### 2.2 Typography
[Google fonts](https://fonts.google.com/) was used to apply the fonts of:

Montserrat - Which is used for the titles.

![Image of Montserrat font with text: Montserrat](/sorteadproject/static/documentation/montserrat-font.png)

Inter - which is used for large bodies of text such as the about section.

![Image of Inter font with text: Inter](/sorteadproject/static/documentation/inter-font.png)

I used [Font Awesome](https://fontawesome.com/) for the icons that shows the gesture for each hand.

### 2.3 Wireframes
I used Frame0 to create my wireframe so that I can visualise the layout of my website. Versions of the site were created for mobile and desktop.

[HomePage Wireframe (Desktop)](/sorteadproject/static/documentation/homepage-wireframe-pc.png)

[HomePage Wireframe (Mobile)](/sorteadproject/static/documentation/homepage-wireframe-mobile.png)

[Booking Page Wireframe (Desktop)](/sorteadproject/static/documentation/booking-page-wireframe-pc.png)

[Booking Page Wireframe (Mobile)](/sorteadproject/static/documentation/booking-page-wireframe-mobile.png)

[Review Page Wireframe (Desktop)](/sorteadproject/static/documentation/review-wireframe-pc.png)

[Review Page Wireframe (Mobile)](/sorteadproject/static/documentation/review-wireframe-mobile.png)

### 3. Features

This website contains multiple pages: The homepage which consists of the about us section and the menu; Theres the booking page which allows the user to book a reservation for the restaurant and theres the login and sign-up pages which allow the user to create and log into an account.

I have used Django framework aswell as bootstrap V5.3 throughout the website to assist in styling the site.

### 3.1 General Features

#### Site Navbar

The first bit of content you will see on the website showcasing the title of the site aswell as the key aspects of it.

![Image of the sites navbar](/sorteadproject/static/documentation/site-navbar.png)

For smaller devices the list of links to other parts of the website are replaced with a dropdown, using a burger icon to reveal it.

![Image of the sites navbar dropdown](/sorteadproject/static/documentation/site-navbar-dropdown.png)

The navbar also changes when a user logs in, switching out the sign-up and login links for a logout link.

![Image of the sites navbar when user is logged in](/sorteadproject/static/documentation/site-navbar-logout.png)

#### Footer

At the bottom of each page contains the footer which has links to different social medias headed by text
saying to "check out our socials!".

![Image of the sites footer](/sorteadproject/static/documentation/site-footer.png)

#### Home Page

The home page holds the most relevant information of the resatuarant, It has been styled so that the information is easy to digest
and readable on any screen.

![Image of the homepage on PC](/sorteadproject/static/documentation/homepage-pc.png)

![Image of the homepage mobile](/sorteadproject/static/documentation/homepage-mobile.png)

#### Menu

The home page also contains the menu for the user to help decide what they would like to eat beforehand, giving them a
smoother experience in the restaurant.

![Image of the menu](/sorteadproject/static/documentation/site-menu.png)

#### User Registration Form

The site contains a form allowing users to register themselves with a username and password also allowing them to create a booking.

![Image of the registration form](/sorteadproject/static/documentation/user-register-form.png)

#### User Login

Once the user has reigstered themselves and logout they can then log back in using their information.

![Image of the User login](/sorteadproject/static/documentation/user-login.png)

#### Booking Page

This page is dedicated to allowing a registered user to reserve themselves a table on a day and time of their choosing
aswell as letting them choose the number of guests (up to 24) and if they have any special requests.

![Image of the booking page](/sorteadproject/static/documentation/booking-form.png)

when the form is filled out and the user clicks the reserve table button, a notification will appear letting 
them know their booking has been accepted.

![Image of the booking notification](/sorteadproject/static/documentation/booking-created.png)

#### Booking Listing Page

below the form is a button that sends the user to a page containing a listing of their bookings where they can choose to edit or delete said bookings.

![Image of the booking listing page](/sorteadproject/static/documentation/booking-listings.png)

#### Update Booking Page

On each listing contains an edit button which takes the user to a seperate page that allows them to change the details of their booking.

![Image of the update booking page](/sorteadproject/static/documentation/update-booking.png)

And if we change the number of guests to 14 then the site updates the listing to show the appropriate number.

![Image of the booking listing update ](/sorteadproject/static/documentation/update-booking-change.png)

#### Delete Booking Page

On each listing also contains a delete button which takes the user to a seperate pages that gives them the choice
to either delete the listing or cancel.

![Image of the delete booking page ](/sorteadproject/static/documentation/delete-booking.png)

And on deletion the user is taken back to the listings page that has now removed the listing.

![Image of the deleted booking ](/sorteadproject/static/documentation/deleted-booking.png)

### 3.2 Future Implementations

I was able to meet most of my user goals within the time frame of this project. I was unable to add the reviews
section but this is because during development i found it unnecessary


In future implementations of this project I would like to make the time slots relate to the tables so that 
if a user books a table at a certain date and time no one else can book it.

### 3.3 Accessibility

Whilst in the process of designing and styling the website, I kept in mind the need to make the page as user friendly and accessible as possible. I have achived this by:
- I used Sans serif font as an alternate font for if my primary font fails to load. 
- I applied the hover function to all of my buttons and used custom styling to ensure the user can tell it is a button.