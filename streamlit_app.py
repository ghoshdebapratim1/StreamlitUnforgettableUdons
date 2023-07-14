#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#import seaborn as sns
import matplotlib.pyplot as plt
#import io
import numpy as np
from wordcloud import WordCloud, STOPWORDS
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet
df = pd.read_csv('movie_statistic_dataset.csv')
df.replace('-', np.nan,inplace=True)
df.dropna(inplace=True)
#Title
st.title("Snaek Movie Data / Film Findings")

## Section 0
st.header('Introduction')
st.write(' We have spent the last 5 days learning about data science and python. We have made a dashboard around a dataset about movies, and we have several graphs to show, so sit back and enjoy the show.')

st.write("Team Members: ")
st.markdown("- Obioma Aguwa")
st.markdown("- Farah Mohamud ")
st.markdown("- Broderic Petermann")
st.markdown("- Gordon Yuan ")
st.markdown("- You Gang Li")

st.header('Section 1 : Data Description and Data Pre-processing')
st.write('Our group is taking a dataset from Kaggle, which contains a comprehensive collection of film data with thousands of inputs. It features information on movie titles, production dates, genres, runtime, and more. To ensure accuracy of our data, we are pre-processing the data by removing missing values.')

st.write(df.head())
# st.subheader('Data Science Workflow')
# st.write('Step 1: Research and capture the data')
# st.write('Step 2: Inspect and clean the data')
# st.write('Step 3: Formulate hypothesis')
# st.write('Step 4: Analyze the data through data visualizations')
# st.write('Step 5: Answer the hypothesis using the visualizations')
# st.write('Step 6: Communicate the results to others')

st.header('Section 2 - Questions related to the dataset')
#Section 1 - Data Inspection and Cleaning
tab1, tab2, tab3, tab4, tab5 = st.tabs(
  ["Obioma", "Farah", "Broderic", "Gordon", "You Gang"])

with tab1:

  ####################################
  ## Obioma

  st.subheader("Which movie genres usually have a longer runtime?")
  df_plot = df.assign(genres=df['genres'].str.split(",")).explode('genres')

  result = pd.DataFrame(
    df_plot.groupby([
      'genres'
    ])['runtime_minutes'].mean().sort_values(ascending=True).reset_index())

  result.columns = ['genres', 'average_runtime']

  result = result[result['genres'] != "\\N"]

  fig = px.bar(result, x='genres', y='average_runtime')

  st.plotly_chart(fig)
  st.write(
    'As you can see from the chart, the movies that tend to have longer runtimes are war and history movies, while animated movies have the shortest runtime. This graph is also mostly uniform, meaning that most movies have around the same amount of runtime'
  )

  st.subheader("Which movie has the highest average rating?")
  topmovie = st.slider('Choose the number of movies you want to show', 0, 50, 5)
  df_plot = df[['movie_title',
                'movie_averageRating']].sort_values(by='movie_averageRating',
                                                    ascending=False).head(topmovie)

  fig = px.bar(df_plot,
               x='movie_title',
               y='movie_averageRating',
               title="Highest Rated Movies")
  st.plotly_chart(fig)
  st.write('This graph features the Top 10 highest rated movies in this dataset with Shawshank Redemption being the highest rated at 9.3. However, this graph is also uniform, so these top movies have close ratings with The Lord of the Rings having an average rating of 8.8.')

  st.subheader(
    "Which movie has the highest worldwide gross profit percentage?")
  df['gross_profit'] = df['Worldwide gross $'] + df['Domestic gross $'] - df[
    'Production budget $']
  df["profit_prc"] = df['gross_profit'] / df['Production budget $']
  df_plot = df[['movie_title',
                "profit_prc"]].sort_values(by="profit_prc",
                                           ascending=False).head(10)

  fig = px.bar(df_plot,
               x='movie_title',
               y="profit_prc",
               title="Top 10 movies with the highest profit percentage")
  st.plotly_chart(fig)
  st.write(
    'The profit percentage was calculated by dividing the gross profit by the production budget. The highest profit percentage made was by Mad Max with 541.5.'
  )
  st.subheader("Which movie has the highest number of votes?")
  fig = px.histogram(df, x='movie_numerOfVotes')
  st.plotly_chart(fig)
  st.write(
    'This data was shown using a histogram and it is heavily skewed to the right'
  )
####################################

## Farah
with tab2:
  st.subheader("Which genre is the most common?")

  df_plot = pd.DataFrame(
    df.genres.str.split(",", expand=True).stack().value_counts().reset_index())
  df_plot.columns = ['genre', 'count']
  fig = px.bar(df_plot, x='genre', y='count')

  st.plotly_chart(fig)
  st.write(
    "The bar graph is in descending order of the most common movie genres. The most common genre is Drama and the least common is News." 
  )

  st.subheader(
    "Does the date the movie was produced on matter in film success?")

  df['gross_profit'] = df['Worldwide gross $'] + df['Domestic gross $'] - df[
    'Production budget $']
  df['production_date'] = pd.to_datetime(df['production_date'])
  df['production_month'] = df['production_date'].dt.month
  df['production_year'] = df['production_date'].dt.year
  df['production_year_month'] = df['production_year'].astype(
    str) + "-" + df['production_month'].astype(str)
  df_plot = df.groupby(
    ['production_month'])['gross_profit'].mean().reset_index().sort_values(
      by='production_month'
    )  #df_plot=df_plot[df_plot['production_year_month']>='2000-01']
  fig = px.line(df_plot, x='production_month', y='gross_profit')
  st.plotly_chart(fig)
  st.write(
    "There seems to be a pattern in the months when movies made the highest gross profit, it's because there is more time for people to watch the movies in the theater."
  )
  st.subheader("What are the average ratings of movies?")
  df_plot = df.assign(genres=df['genres'].str.split(",")).explode('genres')
  fig = px.box(df_plot, x='genres', y='movie_averageRating')
  st.plotly_chart(fig)
  st.write("The median for all movies seems to be in the range from 6 to 8.")
  st.subheader(
    "What is the correlation between the number of votes, average ratings, and approval index?"
  )
  fig = px.scatter_3d(df,
                      x='movie_averageRating',
                      y='approval_Index',
                      z='runtime_minutes',
                      size='approval_Index')
  st.plotly_chart(fig)
  st.write(
    "In the 3d plot you can see the overlapping of the three categories, this might be because they all depend on the audience’s opinions."
  )
####################################

## Broderic

with tab3:
  st.subheader(
    "What is, if any, the correlation between a movies rating and worldwide earnings?"
  )

  fig = px.scatter(x=df['movie_averageRating'],
                   y=df['Worldwide gross $'],
                   title="Movies rating to Money made",
                   labels={
                     'x': "Average rating",
                     'y': 'Worldwide Gross'
                   })

  st.plotly_chart(fig)
  st.write(
    "The graph seems to show an upward relationship between a movie's rating and its worldwide growth"
  )
  st.subheader(
    "What is, if any, the correlations between production budget and worldwide earnings?"
  )

  fig = px.scatter(x=df['Production budget $'],
                   y=df['Worldwide gross $'],
                   title="Movie Money Magic",
                   labels={
                     'x': "Production budget",
                     'y': 'Money made worldwide'
                   })

  st.plotly_chart(fig)
  st.write(
    "The graph dosen't show much correlation between the production budget and worldwide earnings but it does seem that the more money put into the movie the better it performs, with some expections."
  )
  st.subheader("Lowest rated movie genre")
  df_plot = df[['genres',
                'movie_averageRating']].sort_values(by='movie_averageRating',
                                                    ascending=True).head(10)

  fig = px.bar(df_plot,
               x='genres',
               y='movie_averageRating',
               title="Lowest Rated genres")
  st.plotly_chart(fig)
  st.write(
    'The bar graph shows the lowest rated movie genre, with the lowest rated being, comedy, family and science fiction.'
  )

  st.subheader("What percent of the movie industry does each genre take up?")
  df_plot = df.assign(genres=df['genres'].str.split(",")).explode('genres')

  result = pd.DataFrame(
    df_plot.groupby([
      'genres'
    ])['Worldwide gross $'].sum().sort_values(ascending=True).reset_index())

  result.columns = ['genres', 'Total worldwide gross $']

  result = result[result['genres'] != "\\N"]

  fig = px.pie(result,
               values='Total worldwide gross $',
               names='genres',
               title=" Worldwide gross by genre")
  st.plotly_chart(fig)
  st.write(
    "The pie chart makes me hungry, and it shows that the most popular movie genres are adventure and action while other genres such as documentaries are barely even visible on the chart."
  )
  st.subheader("What are Directors' other jobs and their genre?")

  df_plot = df.assign(
    prof=df['director_professions'].str.split(",")).explode('prof')

  df_plot = df_plot.assign(
    genres=df_plot['genres'].str.split(",")).explode('genres')

  df_plot = df_plot.groupby(['prof', 'genres']).size().reset_index()

  df_plot.columns = ['prof', 'genres', 'count']

  fig = px.sunburst(df_plot,
                    path=['prof', 'genres'],
                    values='count',
                    color='prof')
  st.plotly_chart(fig)
  st.write(
    "The Sunburst chart is showing that a directors most common job is directing (Whoa) and then it is being a producer."
  )
  st.write(
    "The second row of the sunburst chart shows what genre has these extra jobs on the director."
  )

####################################

## Gordon
with tab4:
  st.subheader("Which movies have the highest gross profit?")
  topdirectors=st.slider('Choo')
  df_plot = df[['movie_title', 'gross_profit']].head(50)
  
  result = pd.DataFrame(df_plot.groupby(['movie_title', 'gross_profit']).mean().sort_values('gross_profit', ascending=True).reset_index())
  
  result.columns = ['movie_title', 'gross_profit']
  
  fig = px.scatter(df_plot, x='movie_title', y='gross_profit', title='Best Movies by Gross Profit', color="gross_profit", size='gross_profit', hover_data=['movie_title'], labels={'movie_title': 'Movie Title', 'gross_profit': 'Gross Profit'})
  
  st.plotly_chart(fig)
  
  st.write("The movies with the biggest profits are often franchises or related to each other. Another thing I noticed was that the 3 most profitable movies were directed by James Cameron.")
  
  st.subheader("Who are the most common directors in the film industry?")

  df_plot = df['director_name'].value_counts().head(10).reset_index()
  df_plot.columns = ['director_name', 'count']

  fig = px.line(df_plot, x='director_name', y='count', title="Most Common Film Directors", labels={"director_name": "Director Name", "count": "Count"})

  st.plotly_chart(fig)
  # df_plot = df['director_name'].value_counts().head(10).reset_index()
  # df_plot.columns = ['director_name', 'count']
  
  # fig = px.line(df_plot, x='director_name', y='count', title="Most Common Film Directors", labels={"director_name": "Director Name", "count": "Count"})
  
  # st.plotly_chart(fig)
  
  st.write(
      "The top 3 directors with the most films are Steven Spielberg, Clint Eastwood, and Ridley Scott.  ")
    
  st.subheader("What is the average film approval for each production month?")
    
      
  df['production_date'] = pd.to_datetime(df['production_date'])
    
  df['production_month'] = df['production_date'].dt.month
    
  df['production_year'] = df['production_date'].dt.year
    
  df['production_year_month'] = df['production_year'].astype(str) + "-" + df['production_month'].astype(str)
    
  df_plot = df.groupby(['production_month'])['approval_Index'].mean().reset_index().sort_values(by='production_month')
    
  fig = px.bar(df_plot, x='production_month', y='approval_Index', title='Production Month and Approval', labels={"approval_Index": "Approval Index", "production_month": "Production Month"})
  
  st.plotly_chart(fig)
  st.write("After August, film approval increases almost constantly")

####################################
## You Gang
with tab5:
  st.subheader('Which movie genre has the most dead directors?')
  fig = px.scatter(x=df['director_deathYear'], y=df['genres'])
  st.plotly_chart(fig)
  st.write(
    'There seems to be a concentration of dead directors in recent years, and the genres with the most concentration seem to be genres like adventure, action, fantasy, animation, etc.'
  )

  st.subheader('What are the lowest rated movies?')

  df_plot = df[['movie_title',
                'movie_averageRating']].sort_values(by='movie_averageRating',
                                                    ascending=True).head(10)

  fig = px.bar(df_plot,
               x='movie_title',
               y='movie_averageRating',
               title="Lowest Rated Movies")
  st.plotly_chart(fig)

  st.write('The lowest rated movies all have less than 3 out of 10 ratings.')

  st.subheader(
    'Is there a correlation between different numerical values in the data?')
  num_cols = [
    'runtime_minutes', 'movie_averageRating', 'movie_numerOfVotes',
    'approval_Index', 'Production budget $', 'Domestic gross $',
    'Worldwide gross $', 'gross_profit'
  ]

  for col in num_cols:
    df[col] = df[col].astype(float)

  corr_matrix = df[num_cols].corr()

  fig = px.imshow(corr_matrix)

  st.plotly_chart(fig)

  st.write(
    "This is much more interesting. Although there are many very obvious high and low correlation marks, such such as the high correlation between runtime minutes and, well, runtime minutes, there is a surprisingly low correlation between a movie's average rating and its production budget, and at the same time a movie's average rating has a high correlation with its runtime minutes."
  )

# st.subheader('a wordcloud')
# comment_words = ''
# stopwords = set(STOPWORDS)
# movie_list=df.movie_title.unique().tolist()
# # iterate through the csv file
# for val in movie_list:

#     # typecaste each val to string
#     val = str(val)

#     # split the value
#     tokens = val.split()

#     # Converts each token into lowercase
#     for i in range(len(tokens)):
#         tokens[i] = tokens[i].lower()

#     comment_words += " ".join(tokens)+" "

# wordcloud = WordCloud(width = 800, height = 800,
#                 background_color ='white',
#                 stopwords = stopwords,
#                 min_font_size = 10).generate(comment_words)

# # plot the WordCloud image
# fig=plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad = 0)

# st.pyplot(fig)

st.header('Conclusion')

st.write("The data was found on Kaggle in the Dataset The Ultimate Film Statistics. With the table about movies with details about the various aspects of movies such Movie Titles, Production, Genres, Domestic Gross, etc. Using the information we learned this week about Data Science we made an app by analyzing and exploring trends in the film industry to better understand the industry we made Tables, Charts, and Graphs to demonstrate the information we learned about the film industry in a simple way. ")
