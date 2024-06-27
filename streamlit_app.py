import streamlit as st
import pandas as pd


st.title("📊 Data evaluation app")

csv_file = '/workspaces/orangetheory/bquxjob_1c0d9aa4_19055bab559.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)
st.write(df)