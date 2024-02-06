import snowflake.connector
import streamlit
import pandas
client_session_keep_alive = "True"

# Display the table on the page.
streamlit.title('My Parents New Healthy Diner')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Hard-Boiled Free-Range egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello choose fruits:")
streamlit.dataframe(my_data_row)
