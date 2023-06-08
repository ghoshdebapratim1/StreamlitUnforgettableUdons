#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#Title 
st.title("Saucy Salaries")

st.text('More precise depiction among salaries and inter&outer conditions')

## Section 0 
st.header('Introductions')
#adding discription to your website
st.text('Description')

#Section 1 - Data Inspection and Cleaning - Ethan 

## The First 5 rows of the data

## The df.info()

## The Null values - treatment 

## The Dropping Duplicated 

## The standardisation of education level 
st.header('Section 1 : Dataset Inspection and Cleaning')
df = pd.read_csv("Salary_Data.csv")

#showing dataset
st.table(df.head())
st.text('Showing dataset and writting about it here')
# Section 2 - Plotly Visualisation 



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
