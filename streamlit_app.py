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


