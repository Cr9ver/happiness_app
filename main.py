import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("happy.csv")

# Add title
st.title("In search of Happiness")

# Add selectboxes
option1 = st.selectbox("Select the data for the X-axis",("GDP", "Generosity", "Happiness"))

option2 = st.selectbox("Select the data for the Y-axis", ("GDP", "Generosity", "Happiness"))

# match case for option 1
match option1:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# match case for option 2
match option2:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{option1} and {option2}")

# plot data agianast each other
figure = px.line(x= x_array, y=y_array, labels={"x": option1, "y": option2 })
st.plotly_chart(figure)