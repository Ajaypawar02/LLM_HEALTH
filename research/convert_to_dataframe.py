# import mysql.connector
# import pandas as pd

# # Connect to MySQL database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="abstract-programmer",
#   password="example-password", 
#   database = "sumeet_health"
# )
# print(dir(mydb))


# # Query to select data from a table
# query = "SELECT * FROM ingredients_recepie;"

# # Read data from the database into a Pandas DataFrame
# df = pd.read_sql(query, mydb)
# df.head()

# # Close the database connection
# mydb.close()

# # Now, df contains your database table as a Pandas DataFrame
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

from langchain.agents import create_csv_agent
import os
os.environ["OPENAI_API_KEY"] = "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"

# Establish a connection to the MySQL database

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="abstract-programmer",
  password="example-password",
  database="sumeet_health"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute the SQL query to show tables
ans = mycursor.execute("select * from recepie")

# Fetch all the tables from the cursor
tables = mycursor.fetchall()

# Iterate through the tables and fetch all content
# for table in tables:
#     table_name = table[0]
#     print(f"Content of '{table_name}' table:")

# for desc in mycursor.description:
#     print(desc[0])
    
recipe_query = "SELECT * FROM recepie"
mycursor.execute(recipe_query)
recipe_rows = mycursor.fetchall()


new_id_value = 1268 # Replace with the actual new id value
new_name_value = "New Recipe"  # Replace with the actual new name value
new_ingredients_value = "New Ingredient 1, New Ingredient 2"  # Replace with the actual new ingredients value

# Execute the SQL query to insert new values into the 'recepie' table
new_user_added_id = 1268  # Replace with the actual value for user_added_id
insert_query = "INSERT INTO recepie (id, name, ingredients, user_added_id) VALUES (%s, %s, %s, %s)"
insert_values = (new_id_value, new_name_value, new_ingredients_value, new_user_added_id)
mycursor.execute(insert_query, insert_values)


# Commit the changes to the database
mydb.commit()

# Print a message indicating the successful insertion
print(f"New record inserted with ID: {new_id_value}, Name: {new_name_value}, Ingredients: {new_ingredients_value}")

# Close the cursor and connection
mycursor.close()
mydb.close()


