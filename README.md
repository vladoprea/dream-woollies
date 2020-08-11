# Dream Woollies

Dream Woollies e-commerce is a site created as the 4th and last Milestone Project inside Code Institute fullstack developer course. The main purpose of this site is to present and sell wet and needle felted toys and durable accessories made from fine merino wool. All the products are handmade, unique and created from natural materials by a friend of mine.

The app functionality was made using Django3 framework to encourage rapid development. VScode was my choice of code editor. During development, I used sqlite as a database and after deployment on Heroku, I switched to Postgres to ensure that any data entered was visible in my deployed application.

The deployed link for the site is: <https://dream-woollies-ms4.herokuapp.com/>

When testing this app, to make a payment, the following details should be used:

* Card number: 4242 4242 4242 4242
* CVC: any three numbers
* Date: any future date
* ZIP Code: any five numbers

## User Experience(UX)

The site has a smooth and clear functionality. **Customer users** can see a list with all the products, search for products by name or key words in description, see a product details, see other customers reviews. They can adjust their bag by updating quantity or remove items. Additionally, for *customers that registered an account*, they have access to their profile which includes the option to save their delivery details for future use and see their order history. Also, they can leave reviews and ratings.**Business owner** has access to the admin panel that allows them to update products details, price and image, to delete products or add new ones.

All these features were created following these users goals:

### User goals

#### Customer user

Guest customer:

* As a customer, I want to view a list of all the products
* As a customer, I want to see the products on sale or with special offers
* As a customer, I want to filter products based on the collection their in
* As a customer, I want to search a product by name or description
* As a customer, I want to be able to sort products by name, rating or price
* As a customer, I want to see a product details
* As a customer, I want to see reviews and ratings left by other customers
* As a customer, I want to see my bag every time I add a new product
* As a customer, I want to have the ability to adjust the quantity of the items or remove them
* As a customer, I want to make online payments
* As a customer, I want to receive details about my order on email

Registered customer:

* As a registered customer, I want to be able to save my delivery details for future use
* As a registered customer, I want to see my orders history
* As a registered customer, I want to have the option to leave a review and rate any product

Business owner:

* As a business owner, I want to be able to add, remove products and update product details

### Design choices

The design of this site is simple but catchy. It ensures that the products are well represented, call to action buttons have consistency and it is easy to read and navigate as a whole.

#### Fonts

* The font used in this project is [Mulish](https://fonts.google.com/specimen/Mulish), a minimalist Sans Serif typeface from Google Fonts.

#### Colors

* ![#1d1141](https://via.placeholder.com/15/1d1141/000000?text=+) `#1d1141` is the logo color which I used for call to action buttons
* ![#37cec9](https://via.placeholder.com/15/37cec9/000000?text=+) `#37cec9` used for buttons that redirect you to pages or actions regarding products
* ![#ff3b3b](https://via.placeholder.com/15/ff3b3b/000000?text=+) `#ff3b3b` used to draw attention for on sale products
* ![#FFBA00](https://via.placeholder.com/15/FFBA00/000000?text=+) `#FFBA00` main navigation bar
* ![#def5ff4d](https://via.placeholder.com/15/def5ff4d/000000?text=+) `#def5ff4d` background color for home page and products page

### Mock-ups

The mock-ups created for this project are only for 2 types of devices: desktop and mobile. As you can see, the initial mock-ups tend to differ from the final product. This is due to learning more and the desire to make the project more complex. The design was made using Adobe XD.

* [Desktop mock-ups](https://ibb.co/album/BHXpJm)
* [Mobile mock-ups](https://ibb.co/album/JBhs5J)
