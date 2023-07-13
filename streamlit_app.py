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
st.markdown("- Broderic Petermann")
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

df.replace('-', np.nan,inplace=True)

df.dropna(inplace=True)



st.header('Section 2 - Questions related to the dataset')

## Obioma 
st.subheader("which types of movie genres usually have a longer runtime? ")
df_plot=df.assign(genres=df['genres'].str.split(",")).explode('genres')

result = pd.DataFrame(df_plot.groupby(['genres'])['runtime_minutes'].mean().sort_values(ascending=True).reset_index())

result.columns = ['genres', 'average_runtime']


result=result[result['genres']!="\\N"]

fig= px.bar(result,x='genres',y='average_runtime')

st.plotly_chart(fig)

st.subheader("which movie has the biggest average rating?")
df_plot=df[['movie_title','movie_averageRating']].sort_values(by='movie_averageRating',ascending=False).head(10)

fig=px.bar(df_plot,x='movie_title',y='movie_averageRating',title="Highest Rated Movies")
st.plotly_chart(fig)


####################################


## Farah 
st.subheader("Which genre is the most common?")


df_plot = pd.DataFrame(df.genres.str.split(",",expand=True).stack().value_counts().reset_index())
df_plot.columns=['genre','count']
fig=px.bar(df_plot, x='genre',y='count')


st.plotly_chart(fig)


st.subheader("Does the date the movie was produced on matter in film success?")

df['gross_profit']=df['Worldwide gross $']+df['Domestic gross $']-df['Production budget $']
df['production_date']=pd.to_datetime(df['production_date'])
df['production_month']=df['production_date'].dt.month
df['production_year']=df['production_date'].dt.year
df['production_year_month']=df['production_year'].astype(str)+"-"+df['production_month'].astype(str)
df_plot=df.groupby(['production_month'])['gross_profit'].mean().reset_index().sort_values(by='production_month') #df_plot=df_plot[df_plot['production_year_month']>='2000-01']
fig=px.line(df_plot,x='production_month',y='gross_profit')
st.plotly_chart(fig)
st.subheader("What are the average rating of movies?")



## Broderic 


st.subheader("What is if any correlation between a movies rating and worldwide earnings?")

fig = px.scatter(
    x=df['movie_averageRating'],
    y=df['Worldwide gross $'],
    title="Movies rating to Money made",
     labels = {'x':"Average rating",
              'y':'Worldwide Gross'})


st.plotly_chart(fig)

st.subheader("What is, if any, the correlations between production budget and worldwide earnings?")

fig = px.scatter(
    x=df['Production budget $'],
    y=df['Worldwide gross $'],
    title="Movie Money Magic",
     labels = {'x':"Production budget",
              'y':'Money made worldwide'})


st.plotly_chart(fig)
st.subheader("Lowest rated movie genre")
df_plot=df[['genres','movie_averageRating']].sort_values(by='movie_averageRating',ascending=True).head(10)

fig=px.bar(df_plot,x='genres',y='movie_averageRating',title="Lowest Rated genres")
fig.show()

             
## Gordon 
st.subheader("Which movies have the highest gross profit?")
df_plot=df[['movie_title','gross_profit']].sort_values(by='gross_profit',ascending=False).head(10)

result=pd.DataFrame(df_plot.groupby(['movie_title'])['gross_profit'].mean().sort_values(ascending=True).reset_index())

result.columns=['movie_title', 'gross_profit']

fig= px.bar(df_plot,x='movie_title',y='gross_profit', title='Best Movies by Gross Profit')

st.plotly_chart(fig)

st.subheader("Who are the most common directors in the film industry?")
df_plot=df['director_name'].value_counts()[0:10].reset_index()
df_plot.columns=['director_name', 'count']

fig=px.line(df_plot, x='director_name', y='count', title="Most Common Film Directors", labels={
                     "director_name": "Director Name",
                     "count": "Count"})

st.plotly_chart(fig)


## You Gang 
st.subheader('which movie genre has the most dead directors?')
fig = px.scatter(x=df['director_deathYear'], y=df['genres'])
st.plotly_chart(fig)

st.subheader('what are the lowest rated movies?')
df_plot=df[['movie_title','movie_averageRating']].sort_values(by='movie_averageRating',ascending=True).head(10)

fig=px.bar(df_plot,x='movie_title',y='movie_averageRating',title="Lowest Rated Movies")
st.plotly_chart(fig)

st.subheader('Is there a correlation between different numerical values in the data?')
num_cols=['runtime_minutes','movie_averageRating','movie_numerOfVotes','approval_Index','Production budget $','Domestic gross $','Worldwide gross $','gross_profit']

for col in num_cols:
    df[col]=df[col].astype(float)


corr_matrix=df[num_cols].corr()

fig= px.imshow(corr_matrix)

st.plotly_chart(fig)




st.header('Conclusion')
