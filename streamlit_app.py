#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#import seaborn as sns
import matplotlib.pyplot as plt
import io
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

## The Null values - treatment
st.write("# of nulls before removing nulls: ")
st.table(df.isnull().sum())

df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

st.write("# of nulls after removing nulls: ")
st.table(df.isnull().sum())

## The Dropping Duplicated
st.write("Amount of rows before removing duplicated: " + str(df.shape[0]))
df.drop_duplicates(inplace=True)
st.write("Amount of rows after removing duplicated: " + str(df.shape[0]))

## The standardisation of education level
df['Education Level'].replace({"Bachelor's Degree": "Bachelors"}, inplace=True)
df['Education Level'].replace({"Master's Degree": "Masters"}, inplace=True)
df['Education Level'].replace({"Bachelor's": "Bachelors"}, inplace=True)
df['Education Level'].replace({"Master's": "Masters"}, inplace=True)
df['Education Level'].replace({"phD": "PhD"}, inplace=True)

# Section 2 - Plotly Visualisation

st.header('Section 2 : Data Viz')

### Jordyn
st.write('Jordyn')
fig = px.pie(df['Education Level'],
             values=df['Education Level'].value_counts().values,
             names=df['Education Level'].value_counts().index)
fig.update_traces(hoverinfo='label+percent', textinfo='value')
st.plotly_chart(fig)
st.text(
  "Most of the employees within this dataset have a bachelor's degree. The second largest amount of degree holders have a master's degree."
)

fig = px.histogram(df, x="Education Level", color="Gender")
st.plotly_chart(fig)
st.write(
  "More males have bachelor's degrees than females, while females have more master's degrees than males. This shows that more women continue their education after their bachelor's degree. More men continue their education after their master's degree than women."
)

### Maheen
st.write('Maheen')
high_average = df.groupby(
  'Job Title')['Years of Experience'].mean().reset_index()
high_average = high_average.sort_values(by='Years of Experience',
                                        ascending=False).head(10)

fig = px.line(high_average, x='Job Title', y='Years of Experience')
fig.update_xaxes(tickangle=90)
st.plotly_chart(fig)
st.write(
  "The graph shows that higher job positions are typically held by individuals with more years of experience. The line ascends from left to right, indicating that as experience increases, so does the likelihood of occupying a higher position. For example, CEOs usually have around 25 years of experience, while Directors or Principal Engineers have approximately 20 years of experience."
)

min_value = df.groupby('Job Title')['Salary'].min().reset_index()
min_value = min_value.sort_values(by='Salary', ascending=True).head(10)
fig = px.bar(min_value, x='Job Title', y='Salary')
fig.update_xaxes(tickangle=90)
st.plotly_chart(fig)
st.text("")

### Brandon
st.write('Brandon')
max_value = df.groupby('Job Title')[['Salary']].max().reset_index()
max_value = max_value.sort_values(by='Salary', ascending=False).head(10)
fig = px.bar(max_value, x='Salary', y='Job Title', orientation='h')
st.plotly_chart(fig)

### E'Sabel
st.write("E'Sabel")
st.write("Average years of experience  with age")
yoe_df = df[['Age', 'Years of Experience']]
fig = px.scatter(yoe_df)
st.plotly_chart(fig)
st.write("The graph shows that individuals with higher years of experience tend to be older in age. Which illustrate higher paying salaries are people who have more years of experience in the feild")
st.write("Gender roles affect on Salary")
gender_df = df[['Gender', 'Salary']]
fig = px.scatter_matrix(gender_df)
st.plotly_chart(fig)
st.write("Men tend to have higher salaries than women which is shown in the graph. But there are other factors that are consider when having higher paying salaries are the education level. while women tend to go further into getting their degree, men are sometimes paid more than women")
st.write("Most held Job Titles")
fig = px.pie(df['Job Title'],
             values=df['Job Title'].value_counts().values,
             names=df['Job Title'].value_counts().index)
fig.update_traces(hoverinfo='label+percent', textinfo='value')
st.plotly_chart(fig)
st.text("This graph shows that most people have jobs as software engineers. While the second most held jobs are full stack engineer")

#Ethan
st.write('Ethan')
import plotly.graph_objects as go

softwareEngineers = df[df["Job Title"] == "Software Engineer"]
softwareEngineersManager = df[df["Job Title"] == "Software Engineer Manager"]
fullStackEngineer = df[df["Job Title"] == "Full Stack Engineer"]

fig = px.scatter(softwareEngineers,
                 x='Years of Experience',
                 y='Salary',
                 color_discrete_sequence=['red'])
fig2 = px.scatter(softwareEngineersManager,
                  x='Years of Experience',
                  y='Salary',
                  color_discrete_sequence=['blue'])
fig3 = px.scatter(fullStackEngineer,
                  x='Years of Experience',
                  y='Salary',
                  color_discrete_sequence=['green'])

combined_fig = go.Figure()

for trace in fig.data:
  combined_fig.add_trace(trace)

for trace in fig2.data:
  combined_fig.add_trace(trace)

for trace in fig3.data:
  combined_fig.add_trace(trace)

combined_fig.update_layout(
  showlegend=True,
  xaxis_title="Years of Experience",
  yaxis_title="Salary",
  #showlegend=True,
  legend_title="Categories",
  legend=dict(x=0.8, y=0.4, bgcolor='rgba(255, 255, 255, 0.7)'))

combined_fig.add_trace(
  go.Scatter(x=[None],
             y=[None],
             mode='markers',
             marker=dict(color='red'),
             name='Software Engineers'))

combined_fig.add_trace(
  go.Scatter(x=[None],
             y=[None],
             mode='markers',
             marker=dict(color='blue'),
             name='Software Engineer Managers'))

combined_fig.add_trace(
  go.Scatter(x=[None],
             y=[None],
             mode='markers',
             marker=dict(color='green'),
             name='Full Stack Engineers'))

st.plotly_chart(combined_fig)

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
