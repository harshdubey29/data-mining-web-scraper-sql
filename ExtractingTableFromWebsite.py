import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to the database
engine = create_engine('mssql+pyodbc://@HARSH/WebScrapingProj?trusted_connection=yes&driver=SQL+Server')
Session = sessionmaker(bind=engine)
session = Session()

# Define the table model
Base = declarative_base()
class Table(Base):
    __tablename__ = 'tablename'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    info = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)

# Fetch the HTML of the website
url = 'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'
response = requests.get(url)
html = response.text

# Use Beautiful Soup to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table')

# Iterate through each row of the table
for row in table.find_all('tr'):
    # Initialize an empty dictionary to store the data
    data = {}
    # Iterate through each cell of the row
    for cell in row.find_all('td'):
        # Get the text content of the cell
        value = cell.text
        # Get the column name from the cell's parent row
        name = cell.find_previous('th').text
        # Add the name-value pair to the dictionary
        data[name] = value
    if len(data)>0: #check if the data dict is not empty
        # Create a new object of the Table class
        
       
        url = 'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', class_='wikitable sortable')

        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            city = cells[0].text
            population = cells[1].text
            record = Table(name=city,info=population)
            session.add(record)
        session.commit()
