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
## Dropping unnecessary columns
df = df.drop(["Timestamp","Permissions"], axis=1)

## Replace Missing Values 

df['Primary streaming service']=df['Primary streaming service'].fillna(df['Primary streaming service'].mode()[0])
df['Age']=df['Age'].fillna(df['Age'].mean())## Replace Missing Values
df['While working']=df['While working'].fillna(df['While working'].mode()[0])
df['Instrumentalist']=df['Instrumentalist'].fillna(df['Instrumentalist'].mode()[0])
df['Composer']=df['Composer'].fillna(df['Composer'].mode()[0])
df['Foreign languages']=df['Foreign languages'].fillna(df['Foreign languages'].mode()[0])
df['Music effects']=df['Music effects'].fillna(df['Music effects'].mode()[0])
miss_bpm=df[df['BPM'].isnull()==True]
miss_bpm_genre= list(miss_bpm['Fav genre'].unique())
for i in miss_bpm_genre:
  df['BPM']=df['BPM'].fillna( round(df[df['Fav genre']==i]['BPM'].mean(),0) )
## Section 2 - Data Visualisation 


## Yeojoon 

#Music and Insomnia - ba
df_plot=(df.groupby(['Fav genre'])['Insomnia'].mean().reset_index())
df_plot=df_plot.sort_values(["Insomnia"],ascending=True)

fig = px.bar(df_plot, x="Fav genre", y="Insomnia")
st.plotly_chart(fig)

#Music and depressions - Sunburst chart
df["Depression"]=df["Depression"].apply(str)
df_combinations=(df.groupby(["Depression","Music effects","Fav genre"])
                            .size()
                            .reset_index()
                            .rename(columns={0:"count"}))
fig = px.sunburst(df,
                  path=["Depression","Music effects","Fav genre"],
                  title="Which genre most alleviates depression",
                  color="Depression",
                  height = 1000,
                  width = 1000)
st.plotly_chart(fig)

## Devika
#How long people listen to music - histogram
import math
bin_width= 2
nbins = math.ceil((df['Hours per day'].max() - df['Hours per day'].min()) / bin_width)
hours_per_day = px.histogram(df, x='Hours per day', title = 'How Long People Listen to Music')
hours_per_day.update_traces(xbins=dict(
        start=0.0,
        end=24.0,
        size=2
    ))

st.plotly_chart(hours_per_day)

#Favorite genre of music - Pie chart
popular_genre = px.pie(df, names = 'Fav genre', title = 'Favorite Genre of Music')
popular_genre.update_traces(pull=[0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
st.plotly_chart(popular_genre)

#Hours of those who listen while working versus those who don't - bar graph
fig = px.bar(df_plot, x = 'While working', y = 'Hours per day', title = 'Hours per day of those who listen while working versus those who don''t')
st.plotly_chart(fig)

#Music and Anxiety - Heatmap
df['Combo1'] = df['Music effects']+'-'+df['Anxiety'].apply(str)
revised = pd.crosstab(df['Fav genre'], df['Combo1'])
music_anxiety = px.imshow(revised, height = 800, width = 1000, title = 'Music and Anxiety')
st.plotly_chart(music_anxiety)