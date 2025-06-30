# StockCompare
#### Video Demo:  https://youtu.be/P23EPOn8m4w
#### Description:
## Features

* User Login and Registration: Users can create accounts to compare stock symbols and compare stock information between 2 companies.

* Stock Comparison: Users can enter two stock symbols, and the app displays a graph between two stocks.

* Stock Information: Users can view in-depth information about a stock symbols and compare that info with another stock.


## Functionality Breakdown

The application utilizes Flask for routing and templating, Flask-Session for managing user sessions, cs50 for database interactions and operations.

# Routes:
- '/': Renders the login page (login.html).
- '/login': Handles login attempts (POST) and renders the login page (GET).
    * <sub>Login checks a few things while authorizing,such as if the the username already exists in the database,the username and password fields are filled before submitting.</sub>
- '/logout': Clears the user session and redirects to the login page.
- '/signup': Handles user registration (POST) and renders the signup page (GET).
     * <sub>Sign up also checks few things before before allowing user to register,it makes sure all the fields are filled before submitting,Checks if the username already exists in the database.</sub>
- '/compare': Renders the stock comparison page (compare.html). Processes comparison data (POST).
    * <sub>It takes the stock symbols from the user and processes data.By processing I mean it uses the lookup function defined in the samp.py and looks the stock data in through api and plot's the data in a graph using matplotlib library and saves the picture in static folder.</sub>
- '/compare1': Renders the stock comparison page after processing (GET).
    * <sub>After the image is stored from the lookup function unto the static folder /compare1 route displays the image in compare1.html</sub>
    * <sub>It was easy to save the image generated from matplotlib and then display it in the html page than other options.</sub>
- '/info': Renders the stock information page (info.html). Retrieves and displays information about two stocks (GET).
    * <sub>It has a table which has 59 fields and the stocks information are displaayed side by side for ease of comparision.</sub>


# Templates:
- login.html: Login form for user authentication.
- signup.html: Register forrm for user registration.
- compare.html: Form for entering stock symbols for comparison.
- compare1.html: Displays the results of the comparison.It also has a button to compare other stocks,this button will redirect to the
                 compare.html to again compare another stocks.
- info.html: Displays detailed information about two stocks.
- layout.html: It has the layout of the web application.I have used Jinja to extend the same layout for all the webpages.

## Code:
- app.py: This is the main script as the Flask is implemented in this script.This program contains the Flask(Web Framework),SQL(DataBase),
          functions from the samp.py program.

- samp.py : This is where all the api calls are made and data is processed and plotted into graph and then saved into static folder.

## API:
- Yahoo Finance By Api Dojo:I have used this API to get the stock price over the 200 days.

- Stock Analysis By alphawave:I have used this API to get the detailed information about the stock.
