import streamlit as st
import plotly.express as px
import pandas
import os

current_directory = os.getcwd()
print(current_directory)
df = pandas.read_csv("data.txt_1")
print(df)
figure = px.line(x=df["date"],y =df["temperature"],
                 labels={"x":"Date","y":"Temperature (C)"})

st.plotly_chart(figure)