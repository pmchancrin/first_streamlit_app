import snowflake.connector
import streamlit # first_streamlit_app
import pandas

# Display the table on the page.
streamlit.title('My Parents New Healthy Diner')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Hard-Boiled Free-Range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(fruits_to_show)

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')




