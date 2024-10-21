import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as ps
import plotly.graph_objects as go

st.title("Titanic Data Analysis")

df=sns.load_dataset("titanic")

st.dataframe(df)

