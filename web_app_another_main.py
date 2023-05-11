import streamlit as st
import plotly.express as px
import sqlite3
import pandas
import os

# current_directory = os.getcwd()
# print(current_directory)
connection = sqlite3.connect("data_db_1.db")
cursor = connection.cursor()
#date:
cursor.execute("select datetime from temp_data")  # this will give us the date field from the table as a sqlite type
date = cursor.fetchall()  #this will make this a list of tuples or to be specific the values
date = [item[0] for item in date]
print(date)
# temp:
cursor.execute("select temp from temp_data")
temp = cursor.fetchall()
temp = [item[0] for item in temp]
print(temp)

figure = px.line(x=date,y =temp,
                 labels={"x":"Date","y":"Temperature (C)"})

st.plotly_chart(figure)