#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#import seaborn as sns
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet
df = pd.read_csv("Salary_Data.csv")

#Title
st.title("Saucy Salaries")

st.text('More precise depiction among salaries and inter&outer conditions')

## Section 0
st.header('Introductions')
#adding discription to your website
st.text('Description')

#Section 1 - Data Inspection and Cleaning - Ethan

st.header('Section 1 : Dataset Inspection and Cleaning')

## The First 5 rows of the data
st.table(df.head())

## The df.info()
st.table(df.info())

## The Null values - treatment
st.text("Before removing nulls: ")
st.table(df.isnull().sum())

df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

st.text("After removing nulls: ")
st.table(df.isnull().sum())

## The Dropping Duplicated
st.text("Amount of rows before removing duplicated: " + df.shape[0])
df.drop_duplicates(inplace=True)
st.text("Amount of rows after removing duplicated: " + df.shape[0])

## The standardisation of education level

# Section 2 - Plotly Visualisation

st.header('Section 2 : Data Viz')

### Jordyn
fig = px.pie(df['Education Level'],
             values=df['Education Level'].value_counts().values,
             names=df['Education Level'].value_counts().index)
fig.update_traces(hoverinfo='label+percent', textinfo='value')
st.plotly_chart(fig)

### Maheen

fig = px.line(high_average, x='Job Title', y='Years of Experience')
fig.update_xaxes(tickangle=90)
st.plotly_chart(fig)

### Brandon
max_value = df.groupby('Job Title')[['Salary']].max().reset_index()
max_value = max_value.sort_values(by='Salary', ascending=False).head(10)
fig = px.bar(max_value, x='Salary', y='Job Title', orientation='h')
st.plotly_chart(fig)
### E'Sabel

yoe_df = df[['Age', 'Years of Experience']]
fig = px.scatter(yoe_df)
st.plotly_chart(fig)

#SHOWING THE DATA
#dataset Header

#add your dataset (delete dataset this is an example)

#Section 2 - Data Analysis

# st.header('Dataset')
# #Adding images to make your streamlit look visually better!
# st.image('pro.png')
# st.text('You can add photos with descriptions')

# #Adding 3-6 Visualizations using photos collected and made from your graph
# #adding images
# #adding graphs by images
# st.image('pasted image 0.png')
# st.text('Discription about your graph and visualizations')

# #adding graphs by making plotly_Chart
# # Plot!
# #st.plotly_chart(BostonHousing, use_container_width=True)
# #st.text('Discription')

# #adding conclusions
# st.header('Conclusion')
# st.text('add your conclusion here')
