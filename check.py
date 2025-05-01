from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Prompt user for the password securely (password won't be shown in terminal)

# Construct the database URL
db_url = f'postgresql+psycopg2://developer@localhost:5432/booksdb'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except OperationalError as e:
    print(f"Error: Could not connect to the database. Details: {e}")
