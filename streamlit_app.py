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
df = pd.read_csv('mxmh_survey_results.csv')

#Title
st.title("Music and Mental Health")



## Section 0
st.header('Introduction')
st.write('A data analysis on a study that compares the effects between certain music genres and mental health. The following information was derived from an extensive survey with over 700 participants, asking them about things such as their favorite music genres and how often they listen to music, as well as their self-reported effects on mental health, such as anxiety, OCD, insomnia, and depression. In this analysis, we further explored that relationship by creating connections between several different elements of the survey.')

st.write("Team Members: ")
st.markdown("- Devika Kurup ")
st.markdown("- Yeojoon Hur ")



st.header('First few rows of our data ')

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

st.write("") # Yeojoon talk about removing irrelevant and how you replaced  missing values 
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

st.header('Section 2 - Hypothesis or Questions to be answered from the data  ')

st.subheader('Hypothesis 1 : ')
df['isstreamer']=np.where(df['Primary streaming service']=='I do not use a streaming service.','No','Yes')
df_plot=df.groupby(['isstreamer','Exploratory']).size().reset_index()
df_plot.columns=['isstreamer','Exploratory','count']
fig = px.bar(df_plot, x="Exploratory", y="count", color="isstreamer", title="Exploring Music vs Streaming")
st.plotly_chart(fig)

#Favorite Genre of Music - Pie chart - 1st Chart
st.subheader('Hypothesis 4 : ')
popular_genre = px.pie(df, names = 'Fav genre', title = 'Favorite Genre of Music')
popular_genre.update_traces(pull=[0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
st.plotly_chart(popular_genre)

#Hours Per Day - Histogram - 2nd Chart
st.subheader('Hypothesis 3 : ')
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

#Hours of those who listen while working versus those who don't - Bar graph - 3rd Chart 
st.subheader('Hypothesis 5 : ')
df_plot = pd.DataFrame(df.groupby(['While working'])['Hours per day'].mean().reset_index())
fig = px.bar(df_plot, x = 'While working', y = 'Hours per day', title = "Hours per day of those who listen while working versus those who don't")
st.plotly_chart(fig)

#Primary Streaming Service VS Hours Per Day - Histogram - 4th Chart
st.subheader('Hypothesis 1 : ')
df_plot=(df.groupby(['Primary streaming service'])['Hours per day'].mean().reset_index())

fig = px.bar(df_plot, x='Primary streaming service', y='Hours per day')
st.plotly_chart(fig)
#Music and Insomnia - Bar graph
st.subheader('Hypothesis 1 : ')
df_plot=(df.groupby(['Fav genre'])['Insomnia'].mean().reset_index())
df_plot=df_plot.sort_values(["Insomnia"],ascending=True)

fig = px.bar(df_plot, x="Fav genre", y="Insomnia")
st.plotly_chart(fig)

st.write('The chart above explores the relationship between types of music and self-perceived levels of insomnia.On average, those who like listening to rap seem to have the lowest levels of insomnia, while those who like listening to LoFi seem to have the highest levels of insomnia.')

#Music and depressions - Sunburst chart

st.subheader('Hypothesis 2 : ')
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

#Music and Anxiety - Heatmap

st.subheader('Hypothesis 6 : ')
df['Combo1'] = df['Music effects']+'-'+df['Anxiety'].apply(str)
revised = pd.crosstab(df['Fav genre'], df['Combo1'])
music_anxiety = px.imshow(revised, height = 800, width = 1000, title = 'Music and Anxiety')
st.plotly_chart(music_anxiety)

#Music and OCD - Box plot
st.subheader('Hypothesis 7 : ')
music_OCD = px.box(df, x = 'Fav genre', y = 'OCD')
st.plotly_chart(music_OCD)


st.header("Conclusion")

