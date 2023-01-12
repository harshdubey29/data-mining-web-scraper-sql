# data-mining-web-scraper-sql
A web scraper that collects data from websites and stores it in a SQL database. You can use Python libraries such as Beautiful Soup to parse the HTML of web pages and the SQLAlchemy library to interact with the database.

## Introduction

This is a web scraping script that scrapes a wikipedia page containing a list of Indian cities and their population and stores the data in an SQL database. The script uses the python libraries requests, BeautifulSoup, and SQLAlchemy to fetch the HTML of the website, parse it and then insert the data into the SQL database.

## Getting Started

1. Install the dependencies by running 

pip install requests beautifulsoup4 sqlalchemy pyodbc

2. Configure the database connection  by providing the appropriate connection string in the `create_engine` function.
3. Run the script 

python scriptname.py
## Note

This script is set up to use SQL Server as the database and uses the pyodbc driver. If you are using a different database system, you will need to adjust the connection string and possibly the import statements accordingly.

Please make sure to replace the scriptname.py with the actual name of your script file.
