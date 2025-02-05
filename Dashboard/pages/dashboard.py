import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.title("Titanic Data Analysis")

df=sns.load_dataset("titanic")

st.dataframe(df)

st.sidebar.header("Filter Options")
#gender filter
gender=st.sidebar.multiselect('Gender',
                           options=df['sex'].unique(),
                           default=df['sex'].unique())

#class filter
pclass=st.sidebar.multiselect('class',
                              options=sorted(df['pclass'].unique()),
                              default=sorted(df['pclass'].unique()))
#age filter
min_age, max_age=st.sidebar.slider('age',
                                  min_value=int(df['age'].min()),
                                  max_value=int(df['age'].max()),
                                   value = (int(df['age'].min()), int(df['age'].max())))

#filter the dataset based on selection
filtered_data=df[
    (df['sex'].isin(gender))&
    (df['pclass'].isin(pclass))&
    (df['age']>=min_age)&
    (df['age']<=max_age)]

st.subheader("Gender Distribution")
gender_count = filtered_data['sex'].value_counts()
fig = px.pie(names=gender_count.index, values=gender_count.values, title = "Gender Distribution")
st.plotly_chart(fig)

#Create a histogram of age distribution
st.subheader("Age Distribution")
fig = px.histogram(filtered_data, x='age', nbins=20, title = "Age Distribution", 
        labels = {'age': 'Age', 'count': 'Number of Passengers'})
st.plotly_chart(fig)