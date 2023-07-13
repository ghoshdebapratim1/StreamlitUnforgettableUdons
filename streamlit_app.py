#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#import seaborn as sns
import matplotlib.pyplot as plt
import io
import numpy as np 
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet
df = pd.read_csv('movie_statistic_dataset.csv')

#Title
st.title("Snaek Movie Data / Film Findings ")



## Section 0
st.header('Introduction')
st.write(' Write Somethin here ')

st.write("Team Members: ")
st.markdown("- Farah Mohamud ")
st.markdown("- Gordon Yuan ")
st.markdown("- You Gang Li")
st.markdown("-Broderic Petermann")
st.markdown("- Obioma Aguwa")

st.header('Data Description ')
st.write('We got our data from  Kaggle')

st.write(df.head())
# st.subheader('Data Science Workflow')
# st.write('Step 1: Research and capture the data')
# st.write('Step 2: Inspect and clean the data')
# st.write('Step 3: Formulate hypothesis')
# st.write('Step 4: Analyze the data through data visualizations')
# st.write('Step 5: Answer the hypothesis using the visualizations')
# st.write('Step 6: Communicate the results to others')

#Section 1 - Data Inspection and Cleaning
st.header('Section 1 - Data Pre Processing ')







st.header('Section 1 - Questions related to the dataset')

## Obioma 
st.subheader("which types of movie genres usually have a longer runtime? ")
st.subheader("which movie has the biggest average rating?")

## Farah 
st.subheader("Which genre is the most common?")
st.subheader("Does the date the movie was produced on matter in film success?")

## Broderic 
st.subheader("What is if any correlation between a movies rating and worldwide earnings?")
st.subheader("What is, if any, the correlations between production budget and worldwide earnings?")

## Gordon 
st.subheader("Which movies have the highest gross profit?")
st.subheader("Who are the most common directors in the film industry?")


## You Gang 
st.subheader('which movie genre has the most dead directors?')
st.subheader('what are the lowest rated movies?')



st.header('Conclusion')
