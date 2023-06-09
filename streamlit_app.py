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

st.write(
  'More precise depiction among salaries and inter and outer conditions.')

## Section 0
st.subheader('Introductions')
#adding discription to your website
st.write(
  'Our team is called the Pixel Penguins and this is our final project. Over the course of this camp, we have gained an understanding of the programming language "Python" and used that understanding to create interactive data visualizations.'
)
st.write("Team Members: ")
st.markdown("- Brandon Doh ")
st.markdown("- Ethan Chan ")
st.markdown("- E'Sabel Merriweather ")
st.markdown("- Jordyn Russell ")
st.markdown("- Maheen Ali ")

st.subheader('Data Science Workflow')
st.write('Step 1: Research and capture the data')
st.write('Step 2: Inspect and clean the data')
st.write('Step 3: Formulate hypothesis')
st.write('Step 4: Analyze the data through data visualizations')
st.write('Step 5: Answer the hypothesis using the visualizations')
st.write('Step 6: Communicate the results to others')

#Section 1 - Data Inspection and Cleaning - Ethan

st.header('Section 1 : Dataset Inspection and Cleaning')
## The First 5 rows of the data
st.write("First 5 rows of our data set: ")

st.table(df.head())

## The Null values - treatment
st.subheader("Removing Nulls: ")

st.write(
  "We need to remove any NA/missing values as they would mess up any data visualization and other processes later."
)
st.text("")

st.write("Number of nulls before removing nulls: ")
st.table(df.isnull().sum())

df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

st.write("Number of nulls after removing nulls: ")
st.table(df.isnull().sum())

## The Dropping Duplicated
st.subheader("Removing Duplicate Rows: ")

st.write("In order to get cleaner data, we can remove duplicate rows.")
st.text("")

st.write("Amount of rows before removing duplicated: " + str(df.shape[0]))
df.drop_duplicates(inplace=True)
st.write("Amount of rows after removing duplicated: " + str(df.shape[0]))

## The standardisation of education level
st.subheader("Standardizing Education Levels:")

st.write(
  "In education levels, there are many cases where there is two things that mean the same thing, but are typed differently, like Bachelor's Degree and Bachelor's, they are considered different to the program. So by standardizing, we can make sure the computer doesnt end up seperating them."
)
st.text("")

st.write("Before standardization: ")
st.table(df["Education Level"].value_counts())

st.text("Bachelor's Degree and Bachelor's   =>   Bachelors")
st.text("Master's Degree and Master's       =>   Masters")
st.text("phD                                =>   PhD")
st.text("")

df['Education Level'].replace({"Bachelor's Degree": "Bachelors"}, inplace=True)
df['Education Level'].replace({"Master's Degree": "Masters"}, inplace=True)
df['Education Level'].replace({"Bachelor's": "Bachelors"}, inplace=True)
df['Education Level'].replace({"Master's": "Masters"}, inplace=True)
df['Education Level'].replace({"phD": "PhD"}, inplace=True)

st.write("After standardization: ")
st.table(df["Education Level"].value_counts())

# Section 2 - Plotly Visualisation

st.header('Section 2 : Data Viz')

### Jordyn
st.subheader('Jordyn')

st.subheader(
  "Hypothesis 1: What is the amount of employees in each Education Level?")
st.write("Each slice of this pie chart represents a different value.")
fig = px.pie(df['Education Level'],
             values=df['Education Level'].value_counts().values,
             names=df['Education Level'].value_counts().index)
fig.update_traces(hoverinfo='label+percent', textinfo='value')
st.plotly_chart(fig)
st.write(
  " This chart shows that most of the employees within this dataset have a bachelor's degree. The second largest amount of degree holders have a master's degree. The least populated education level is high school."
)

st.subheader(
  "Hypothesis 2: For each Education Level, what is the Gender make-up?")
st.write("Each color on this histogram represents a different Gender.")
fig = px.histogram(df, x="Education Level", color="Gender")
st.plotly_chart(fig)
st.write(
  "This graph shows that more males have bachelor's degrees than females, while females have more master's degrees than males. More women continue their education after their bachelor's degree. More men continue their education after their master's degree than women."
)

st.subheader(
  "Hypothesis 3: What fifteen Job Titles have the highest average Age?")
st.write("Each bar on this barplot corresponds tiwh a different Job Title.")
averageAge = df.groupby("Job Title")[["Age"]].mean().reset_index()
averageAge = averageAge.sort_values(by="Age", ascending=False).head(15)
fig = px.bar(averageAge, x="Job Title", y="Age")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)
st.write(
  "This graph illustrates that the job titles with the highest average age are Director and CTO, both having the value 52. The average age of these fifteen titles range from 47 to 52."
)

### Maheen
st.subheader('Maheen')
st.subheader(
  'Hypothesis 4: Correlation bewteen Years of Experience and Job Titles')

st.write(
  "The line graph depicts the relationship between years of experience and the job title a person can hold.  The  x - axis represents job titles, while the y - axis represents years of experience."
)

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

st.subheader("Hypothesis 5: How different Job Titles will affect the Salary")
st.write(
  "The bar chart compares salary ranges across various job titles. Each bar represents a job title, with its height indicating the corresponding salary range."
)

min_value = df.groupby('Job Title')['Salary'].min().reset_index()
min_value = min_value.sort_values(by='Salary', ascending=True).head(10)
fig = px.bar(min_value, x='Job Title', y='Salary')
fig.update_xaxes(tickangle=90)
st.plotly_chart(fig)

st.write(
  "From this graph, we can observe that certain job titles, such as sales representatives, tend to have higher salaries compared to positions like junior HR coordinators. The chart clearly demonstrates the disparity in salary ranges between different job titles. "
)

### Brandon
st.subheader('Brandon')
st.subheader(
  'Hypothesis 6: there exisit a correlation between Salaries and Job Titles')
max_value = df.groupby('Job Title')[['Salary']].max().reset_index()

max_value = max_value.sort_values(by='Salary', ascending=False).head(10)

fig = px.bar(max_value, x='Salary', y='Job Title', orientation='h')
st.plotly_chart(fig)

st.write(
  'This graph shows the correlation between the Job titles and Salaries. Through this graph we were able to perceive that jobs like CEOs and cheif technology officers were able to make the most Salaries by about 250,000 while the jobs like senior product managers had the least Salaries. by about 200,000.'
)
st.subheader('Hypothesis 7: correlation between education, age and salary')

df['Education Level'] = df['Education Level'].replace({
  "Bachelor's Degree": "Bachelor's",
  "Master's Degree": "Master's",
  "PhD": "phD"
})
temp_df = df[['Age', 'Salary', 'Education Level']]
fig = px.scatter(temp_df, x='Age', y='Salary', color='Education Level')
st.plotly_chart(fig)
st.write(
  'The scatterplot shows that there is relationship between Education level and Salary. those who completed their PhD tend to have a lighter color at a earlier age and gradually the salary from a PhD to a High School graduate. As the brightness of the dots resemble the amount of salaries we are able to depict that the amount of salaries that those who completed their PhD has a bigger salary at a young age than those who completed their masters or bachelors degreee'
)

### E'Sabel
st.subheader("E'Sabel")
st.subheader(" Hypothesis 8: Average years of experience  with age")
yoe_df = df[['Age', 'Years of Experience']]
fig = px.scatter(yoe_df, x='Age', y='Years of Experience')
st.plotly_chart(fig)
st.write(
  "The graph shows that individuals with higher years of experience tend to be older in age. Which illustrate higher paying salaries are people who have more years of experience in the feild"
)
st.subheader("Hypothesis 9: Gender roles affect on Salary")
gender_avg_salary = df.groupby('Gender')['Salary'].mean().reset_index()

fig = px.Bar(x=gender_avg_salary['Gender'], y=gender_avg_salary['Salary'])

fig.update_layout(title="Average Salary by Gender",
                  xaxis_title="Gender",
                  yaxis_title="Average Salary")

st.plotly_chart(fig)
st.write(
  "Men tend to have higher salaries than women which is shown in the graph. But there are other factors that are consider when having higher paying salaries are the education level. while women tend to go further into getting their degree, men are sometimes paid more than women"
)
st.subheader("Hypothesis 10: Top ten Most held Job Titles")
topTen = df["Job Title"].value_counts()[:10]
fig = px.bar(df, x=topTen.values, y=topTen.index, orientation='h')
fig.update_layout(xaxis_title='Number of Employees', yaxis_title='Job Titles')
st.plotly_chart(fig)
st.write(
  "This graph shows that most people have jobs as software engineers. While the second most held jobs are full stack engineer"
)

#Ethan
st.subheader('Ethan')
st.subheader(
  "Hypothesis 11: People can be promoted to a higher position of their job after obtaining years of experience."
)

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
  legend=dict(x=0.8, y=0.3, bgcolor='rgba(255, 255, 255, 0.7)'))

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

st.write(
  "There seems to be a decrease of software and full stack engineers and an increase of software engineer managers as the years of experience goes up. This most likely signifies that at around 12 years of experience is when a lot of software and fullstack engineers start to become managers."
)

## Summary
st.subheader("Summary")
st.subheader('Overall Goal of the project')
st.write(
  'The overall goal of this project was to inspect the overall flow job employment. Because of the fast development of AI chatbots, many professionals expect that many jobs would be replaced. To compare this clearly, we decided to analyze old datasets, and through these close inspections of old data sets, we would be able to predict the future job employment flow.'
)

st.markdown(
  "Hypothesis 1 overview: This pie chart shows the number of employees within this dataset who have bachelor's and master's degree. Which the most held degree is bachelor's degree."
)

st.markdown(
  "Hypothesis 2 overview: This graph shows the education levels of genders. We discover that males have more bachelor's degrees than females. While females continue their education and have more master's degrees."
)

st.markdown(
  "Hypothesis 3 overview: This bar chart shows the 15 Job titles and their correlate age. We can conclude from the graph that employees with positions like Chief Technology Officer and Director are older in age than someone who is a Supply Chain analyst. "
)

st.markdown(
  "Hypothesis 4 overview: this shows the relationship between years of experience and job titles through a line graph. What we understand from the graph is higher job positions are held by individuals that have more years of experience. In the graph you can see as the experience an individual has increases,so does the occupying higher positions."
)

st.markdown(
  "Hypothesis 5 overview: In the bar graph we see various job titles with its corresponding salary range. Observed within the graph certain job titles that are ranked higher tend to have higher salaries compared to job titles that are ranked lower."
)

st.markdown(
  "Hypothesis 6 overview: In this graph we can get an insight of the correlation bewteen Salaries and Job Titles. We can interpet from this graph that CEOs and Cheif Technology Officers are making around 250,000 while jobs like Prfo "
)

st.markdown(
  "Hypothesis 7 overview: This graph would show what level of education or age woule one get a certain amount of salary"
)

st.markdown(
  "Hypothesis 8 overview: In the scatterplot we are able to observe the correlation between education level like individuals with PhD have a lighter color tend to have higher salaries. While age also plays a role individuals i"
)
st.markdown(
  "Hypothesis 9 overview: In the graph, w are able to perceive the correlation between sex and amount of salary. As a result, there seems to have a minor salary difference between male and female."
)

st.markdown(
  "Hypothesis 10 overview: the number of employees on each job title")
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
