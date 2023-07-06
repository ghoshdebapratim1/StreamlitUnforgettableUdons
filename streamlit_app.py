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
df = pd.read_csv('mxmh_survey_results.csv')

#Title
st.title("Music and Mental Health")

st.write('Effect of music on mental health conditions')

## Section 0
st.subheader('Introductions')
#adding discription to your website
st.write('Some title for some dashboard ')
st.write("Team Members: ")
st.markdown("- Devika Kurup ")
st.markdown("- Yeojoon Hur ")

# st.subheader('Data Science Workflow')
# st.write('Step 1: Research and capture the data')
# st.write('Step 2: Inspect and clean the data')
# st.write('Step 3: Formulate hypothesis')
# st.write('Step 4: Analyze the data through data visualizations')
# st.write('Step 5: Answer the hypothesis using the visualizations')
# st.write('Step 6: Communicate the results to others')

#Section 1 - Data Inspection and Cleaning

st.write(df.head())
