## Testing

### Testing User Stories
#### Testing User Goals
| Goal                                                | Result  | Comment                                                                                                              |
|-----------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------|
| Take online bookings     | Success | The site is capable of taking bookings. |
| Book multiple guests     | Success | The sites booking page allows for multiple guests to be added to a reservation. |
| Review section | Failure | This feature was scrapped during development. |
| Cancellations            | Success | The sites provides the user the ability to cancel their bookings once made.  |
| Menu           | Success | The sites provides the user with a menu for food and drink.  |

### Bugs

Throughout the development of the site I have been consistently checking for bugs or issues in the code some of those issues are as followed:

- The background image on the homepage was not loading and the solution to this was to load static in the home.html file

- The burger icon for when the sites viewport is shrunk down enough wasnt showing up and I solved this by installing bootstrap icons and then using the list icon as a substitute

- Theres an bug where when a user books a table no more bookings can be made for that table, while i was unable to solve this in my timeframe I would solve it as a future implementation.

### Manual Testing
I have manually tested each key feature on the site to ensure they have the proper functionality.

![Gif of navbar test](/sorteadproject/static/documentation/navbar-test.gif)
![Gif of signup test](/sorteadproject/static/documentation/signup-test.gif)
![Gif of login test](/sorteadproject/static/documentation/login-test.gif)
![Gif of update test](/sorteadproject/static/documentation/update-test.gif)
![Gif of delete test](/sorteadproject/static/documentation/delete-test.gif)

#### Funcitonality testing

- The testing was completed on the following devices:

- Personal Computer
- Iphone 16e

The browsers used to test the site include:

- Google Chrome
- Safari
- Microsoft Edge

### Lighthouse
I have used the "lighthouse" feature within Chrome dev tools to test the sites performance, accessibility and best practices. I have checked both mobile and desktop device types.

#### homepage 

![image of home-page lighthouse performance for desktop](/sorteadproject/static/documentation/homepage-lighthouse-pc.png)

Initial lighthouse testing diagnostics show that the main fault on both desktop and mobile is the menu image element doesnt contain explicit width and height. 
to try and rectify this I set them both to auto as setting them to a definitive height and width caused the menu to get smushed when
shrunken down and near impossible to read yet the fault still remained so I decided to keep the fault as I felt that the site
still functioned well. 

#### Booking page

![image of booking-page lighthouse performance for desktop](/sorteadproject/static/documentation/booking-lighthouse-pc.png)
![image of booking-page lighthouse performance for mobile](/sorteadproject/static/documentation/booking-lighthouse-pc.png)

Initial lighthouse testing diagnostics for the booking page show no issues on both desktop and mobile.

#### Sign-up page

![image of sign-up page lighthouse performance for desktop](/sorteadproject/static/documentation/signup-lighthouse-pc.png)
![image of sign-up page lighthouse performance for mobile](/sorteadproject/static/documentation/signup-lighthouse-pc.png)

Initial lighthouse testing diagnostics for the sign up page show no issues on both desktop and mobile.

#### Login page

![image of login page lighthouse performance for desktop](/sorteadproject/static/documentation/login-lighthouse-pc.png)
![image of login page lighthouse performance for mobile](/sorteadproject/static/documentation/login-lighthouse-pc.png)

Initial lighthouse testing diagnostics for the booking page show no issues on both desktop and mobile.

#### Booking listing page

![image of booking listing page lighthouse performance for desktop](/sorteadproject/static/documentation/login-lighthouse-pc.png)
![image of booking listing page lighthouse performance for mobile](/sorteadproject/static/documentation/login-lighthouse-pc.png)

Initial lighthouse testing diagnostics for the booking listing page show minimal issues and need no changing.

#### Update listing page

![image of update listing page lighthouse performance for desktop](/sorteadproject/static/documentation/update-lighthouse-pc.png)
![image of update listing page lighthouse performance for mobile](/sorteadproject/static/documentation/update-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the update listing page show minimal issues and need no changing.

#### Delete listing page

![image of delete listing page lighthouse performance for desktop](/sorteadproject/static/documentation/delete-lighthouse-pc.png)
![image of delete listing page lighthouse performance for mobile](/sorteadproject/static/documentation/delete-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the delete listing page show the accessibilty issues for pc are not up to par. The main issue
being the logout button was not apart of the list in the nav causing the screen reader to have issues, therefore I simply added the logout 
to the list and it was solved.

![image of delete listing page lighthouse performance for desktop](/sorteadproject/static/documentation/delete-lighthouse-pc-fixed.png)

### Validation

[W3C](https://validator.w3.org/) validator has been used to check the HTML.

[W3C](https://jigsaw.w3.org/css-validator/) jigsaw has been used to check the CSS stylesheet. 

#### HTML

##### Home page

The initial check in the source for the home page came up with an error which was solved by simply removing a stray end div tag

![image of home page validation](/sorteadproject/static/documentation/homepage-validation.png)

##### Booking page

The initial check in the source for the booking page came up with an error which was solved changing the button with a url into 
a form containing a button and having the forms action be the href

![image of booking page validation](/sorteadproject/static/documentation/booking-page-validation.png)

##### Booking listing page

The initial check in the source for the booking listing page came up with an error which was solved changing the button with a
url into a form containing a button and having the forms action be the href

![image of booking listing page validation](/sorteadproject/static/documentation/listing-page-validation.png)

##### Update booking page

The initial check in the source for the update booking page came up with zero errors so no change was needed.

![image of update booking page validation](/sorteadproject/static/documentation/update-validation.png)

##### Delete booking page

The initial check in the source for the delete booking page came up with an error which was solved by adding an onclick to 
the button to redirect it to the homepage and have the button type set as button so it doesnt submit the form its already in.

![image of delete booking page validation](/sorteadproject/static/documentation/delete-validation.png)

##### Sign up page

The initial check in the source for the sign up page came up with zero errors so no change was needed.

![image of sign up page validation](/sorteadproject/static/documentation/update-validation.png)

##### Login page

The initial check in the source for the login page came up with zero errors so no change was needed.

![image of login page validation](/sorteadproject/static/documentation/update-validation.png)

#### CSS

The initial check for the css code came up with zero errors so no change was needed.

![image of css validation](/sorteadproject/static/documentation/css-validation.png)