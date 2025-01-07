import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv("vehicles_us.csv")

data.info()
st.header("Interactive Data Dashboard")

st.subheader("Histogram of Data")
fig_hist = px.histogram(data, x="model_year", title="Histogram of Model Year")  
st.plotly_chart(fig_hist)

st.subheader("Histogram of Data")
fig_hist = px.histogram(data, x="paint_color", title="Histogram of paint color")  
st.plotly_chart(fig_hist)

