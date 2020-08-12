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

The site has a smooth and clear functionality. **Customer users** can see a list with all the products, search for products by name or key words in description, see a product details, see other customers reviews. They can adjust their bag by updating quantity or remove items. Additionally, for *customers that registered an account*, they have access to their profile which includes the option to save their delivery details for future use and see their order history. Also, they can leave reviews and ratings. **Business owner** has access to the admin panel that allows them to update products details, price and image, to delete products or add new ones.

All these features were created following these users goals:

### User goals

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

## Features

### Existing features

#### Header and navigation bar

* logo on the top left with link to home page. Visible only on large screens
* search bar for looking after products by name or key words in description. On smaller than large screens, it transforms into a search icon, which when selected opens into a search bar
* social icons for Facebook, Instagram and Pinterest visible only on large screens
* My account icon with dropdown list of options for register and login. When registered, the dropdown list contains profile and logout links
* Bag icon with link to your bag list items and the total price of the selected order

#### Home page

* first section consists in a background picture, name of the brand, a short description and a call to action button that redirects to all products page
* second section is formed by 4 products that are on sale, and a bar with a link to the page of all on sale products
* third section is formed by image link cards for each collection of products available on site: Wool Paintings, Brooches, Toys, Christmas Deco and Home Deco. There is also a image link card with all products

#### All Products

* contains a list of all products available displayed using pagination. There are 12 products of each page and at the bottom you find the pagination navigation links
* at the top, there are 5 badges that act as filters for each collection available on the site. When choosing a collection, the badge change color to help user to know where it is in that moment
* sorting option for prices, rating and name in ascending or descending way

#### ON SALE

* contains a list with all the products that are on sale at that moment

#### Product detail

* when choosing one specific product, a new page opens that contains the chosen product, its details, input quantity option and a button to add it to bag
* reviews and ratings left by registered users

##### Reviews

* on product detail page, a registered user has the option to leave a review and to rate the product. This is made via a form that has an input field for ratings with options from no rating to 5. The average of ratings is displayed on each product details list

#### Bag

* on the bag page, the user can see its selected products displayed on top of each other. Each product from the bag contains its image, name, price, quantity selected and the subtotal which is price multiplied by quantity
* the user has the option to update each products quantity or remove it
* on bottom right of the page, the grand total with delivery included is displayed and two buttons. One to proceed to checkout and one to go back and shop more

#### Checkout

* contains a form for the delivery details of the user
* contains the payment form from Stripe that takes: card number, CVC, expiry date and ZIP code
* contains an order summary, as a table with products name, quantity selected, subtotal. Also, the delivery costs, grand total and a button that redirects to bag for adusting it if needed. This feature is not available on small devices.

#### Emails

* user receives an email on the email address provided with details of his order

#### Register and login

* form for register with: email address, username, password fields
* form for login with: email address or username, password fields
* confirmation email for registering
* option to change password

#### Profile

* this is available only for registered users. It contains a form with delivery details of the user that can be updated and saved for future use and a table for order history which contains: order number, name of the products and quantity selected, date when the order was registered and total

#### Contact

* contains the contact details of the business: email and phone number
* contains a form for message

#### Footer

* contains links to about me and contact page
* contains social media icon links for Facebook, Instagram and Pinterest
* contains icons for cards accepted and payment security provider
* contains copyright

### Future features

* Product management for business owners.  The ability to add, edit, delete a product from a customized, more friendly interface. This can be done from the admin panel in the meantime.
* Update or remove an own review as a registered user.
* The ability to choose more than one filters at once. The option to disable a filter if user click on it.

## Technologies

### Tools

* [VSCode](https://code.visualstudio.com/) - as code editor
* [GIT](https://git-scm.com/) - to manage version control
* [GitHub](https://github.com/) - to share and store code remotely
* [Heroku](https://heroku.com/) - for hosting the application and deployment
* [AWS S3](https://aws.amazon.com/s3/) - cloud service for media and static files
* [Stripe](https://stripe.com/) - for managing payments
* [Sqlite3](https://www.sqlite.org/index.html) - database for development
* [PostgreSQL](https://www.postgresql.org/) - database provided by Heroku for production
* [AdobeXD](https://www.adobe.com/products/xd.html) - for creating mock-ups

### Libraries and frameworks

* [Django3](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development
* [Bootsrap4](https://getbootstrap.com/) - for layout and responsive design
* [FontAwesome](https://fontawesome.com/) - icons implementation
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - a template language for python used to bring logic into templates
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - a library that enables python code to modify AWS service

### Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Tesing

## Deployment

This application can run locally or deployed to a live environment

### Local

The example provided uses VSCode as a code editor and Windows as an operating system.

1. Save a copy of the github repository located at <https://github.com/vladoprea/dream-woollies> by clicking the 'download.zip' button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command:

```python
git clone <https://github.com/maliahavlicek/ms4_challenger.git>
```

1. Set up a virtual environment via this command in the terminal session:

```python
python -m venv env
```

1. Activate the .venv with the command:

```python
\env\Scripts\activate.bat
```

1. Install all required modules with the command:

```python
pip install -r requirements.txt
```

1. Create a env.py file and add it to your .gitignore

1. Copy the following into the env.py file:

```python
import os

os.environ['SECRET_KEY'] = 'your value'
os.environ['DATABASE_URL'] = 'your value'
os.environ['STRIPE_PUBLIC_KEY'] = 'your value'
os.environ['STRIPE_SECRET_KEY'] = 'your value'
os.environ['STRIPE_WH_SECRET'] = 'your value'
os.environ['AWS_ACCESS_KEY_ID'] = 'your value'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your value'
os.environ['DEVELOPMENT'] = '1'
```

1. Set up the databases by running the following management command in your terminal:

```python
python manage.py migrate
```

1. Create the superuser so you can have access to the django admin:

```python
python manage.py createsuperuser
```

1. Start your server by running the following command in your terminal:

```python
python manage.py runserver
```

### Deploy to Heroku

The deployed site can be found here: <https://dream-woollies-ms4.herokuapp.com/>

1. Login to Heroku and create a new app

1. On the Resources tab, in the Add-ons field look for Heroku Postgres, select the default Hobby Dev - Free
tier, then click the Provision button. This will provision a Postgres Database for you.

1. In Heroku, go on settings tab and click Reveal Config Vars.

1. Add the values from your env.py file to heroku:

```python
AWS_ACCESS_KEY_ID - your value
AWS_SECRET_ACCESS_KEY - your value
DATABASE_URL - your value
EMAIL_HOST_PASS - your value
EMAIL_HOST_USER - your value
SECRET_KEY - your value
STRIPE_PUBLIC_KEY - your value
STRIPE_SECRET_KEY - your value
STRIPE_WH_SECRET - your value
USE_AWS - True
```

1. Set up the databases with the following command:

```python
python manage.py migrate
```

1. Create the superuser for the postgres database so you can have access to the django admin:

```python
python manage.py createsuperuser
```

1. Preload products and collections using following commands(the order is important):

```python
python manage.py loaddata collections.json
python manage.py loaddata products.json
```

1. Save all the requirements:

```python
pip freeze > requirements.txt
```

1. Create Procfile:

```python
echo web: gunicorn dream_woollies.wsgi:application > Procfile
```

1. Add the files and push them to Github:

```python
git add .
git commit
git push
```

1. Deploy branch in Heroku

1. In settings.py add <https://dream-woollies-ms4.herokuapp.com/> to Allowed Hosts

## Credits

### Media

All the images and texts were provided by Ioana Cucoreanu which is the rightful owner of their copyright.

### Code

* A big part of the code was developed by following the Code Institute video lessons. Where needed, I provided credits in the comments of the code.
* [StackOverflow](https://stackoverflow.com/) where I found answers for different topics
* Average rating was inspired following this video: <https://www.youtube.com/watch?v=rca4ZNFnh5M&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk&index=29>

### Acnowledgements

* Code Institute Slack Community for providing solutions to every question I had.
* Tutoring from Code Institute that was very patient and heplful when I was in need.

Special thanks to Maranatha Ilesanmi, my mentor, who guided me through this project and provided punctual, solid, useful feedback and very helpful input and tips
