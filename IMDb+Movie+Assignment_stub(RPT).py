#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Filtering out the warnings

import warnings

warnings.filterwarnings('ignore')


# In[7]:


# Importing the required libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # <font color = blue> IMDb Movie Assignment </font>
# 
# You have the data for the 100 top-rated movies from the past decade along with various pieces of information about the movie, its actors, and the voters who have rated these movies online. In this assignment, you will try to find some interesting insights into these movies and their voters, using Python.

# ##  Task 1: Reading the data

# - ### Subtask 1.1: Read the Movies Data.
# 
# Read the movies data file provided and store it in a dataframe `movies`.

# In[256]:


# Read the csv file using 'read_csv'. Please write your dataset location here.
movies=pd.read_csv("C:\\Users\\MANLAP02\\Downloads\\Movie+Assignment+Data.csv")
movies.head()


# - ###  Subtask 1.2: Inspect the Dataframe
# 
# Inspect the dataframe for dimensions, null-values, and summary of different numeric columns.

# In[247]:


# Check the number of rows and columns in the dataframe
movies.shape


# In[248]:


# Check the column-wise info of the dataframe
movies.info()


# In[249]:


# Check the summary for the numeric columns 
movies.describe()


# In[250]:


movies.isnull().sum()


# ## Task 2: Data Analysis
# 
# Now that we have loaded the dataset and inspected it, we see that most of the data is in place. As of now, no data cleaning is required, so let's start with some data manipulation, analysis, and visualisation to get various insights about the data. 

# -  ###  Subtask 2.1: Reduce those Digits!
# 
# These numbers in the `budget` and `gross` are too big, compromising its readability. Let's convert the unit of the `budget` and `gross` columns from `$` to `million $` first.

# In[257]:


# Divide the 'gross' and 'budget' columns by 1000000 to convert '$' to 'million $'
movies['Gross']=movies['Gross']/1000000
movies['budget']=movies['budget']/1000000
movies.head()


# -  ###  Subtask 2.2: Let's Talk Profit!
# 
#     1. Create a new column called `profit` which contains the difference of the two columns: `gross` and `budget`.
#     2. Sort the dataframe using the `profit` column as reference.
#     3. Extract the top ten profiting movies in descending order and store them in a new dataframe - `top10`.
#     4. Plot a scatter or a joint plot between the columns `budget` and `profit` and write a few words on what you observed.
#     5. Extract the movies with a negative profit and store them in a new dataframe - `neg_profit`

# In[258]:


# Create the new column named 'profit' by subtracting the 'budget' column from the 'gross' column
movies['profit']=movies['Gross']-movies['budget']
movies.head()


# In[21]:


# Sort the dataframe with the 'profit' column as reference using the 'sort_values' function. Make sure to set the argument
#'ascending' to 'False'
movies.sort_values(by=['profit'],ascending=False, inplace=True, ignore_index=True)
movies.head()


# In[27]:


# Get the top 10 profitable movies by using position based indexing. Specify the rows till 10 (0-9)

top10=movies.loc[0:9,'Title']
top10


# In[43]:


#Plot profit vs budget
plt.figure(figsize=[10,8])
sns.jointplot(x='budget',y='profit',data=movies,color='red')
plt.suptitle('Scatter plot budget and profit')
plt.show()


# In[ ]:


## Observation 
-> Most of the movies have positive profit & also budgets are high
-> There are some movies having high budget but having negative profit
-> Between 0-100 million budget, a good number of movies provide profit ranging 0-300 million dollors(Exclude negative profit movies)


# In[ ]:





# The dataset contains the 100 best performing movies from the year 2010 to 2016. However, the scatter plot tells a different story. You can notice that there are some movies with negative profit. Although good movies do incur losses, but there appear to be quite a few movie with losses. What can be the reason behind this? Lets have a closer look at this by finding the movies with negative profit.

# In[44]:


#Find the movies with negative profit
neg_profit=movies[movies['profit']<0]
neg_profit.reset_index(drop=True)


# **`Checkpoint 1:`** Can you spot the movie `Tangled` in the dataset? You may be aware of the movie 'Tangled'. Although its one of the highest grossing movies of all time, it has negative profit as per this result. If you cross check the gross values of this movie (link: https://www.imdb.com/title/tt0398286/), you can see that the gross in the dataset accounts only for the domestic gross and not the worldwide gross. This is true for may other movies also in the list.

# - ### Subtask 2.3: The General Audience and the Critics
# 
# You might have noticed the column `MetaCritic` in this dataset. This is a very popular website where an average score is determined through the scores given by the top-rated critics. Second, you also have another column `IMDb_rating` which tells you the IMDb rating of a movie. This rating is determined by taking the average of hundred-thousands of ratings from the general audience. 
# 
# As a part of this subtask, you are required to find out the highest rated movies which have been liked by critics and audiences alike.
# 1. Firstly you will notice that the `MetaCritic` score is on a scale of `100` whereas the `IMDb_rating` is on a scale of 10. First convert the `MetaCritic` column to a scale of 10.
# 2. Now, to find out the movies which have been liked by both critics and audiences alike and also have a high rating overall, you need to -
#     - Create a new column `Avg_rating` which will have the average of the `MetaCritic` and `Rating` columns
#     - Retain only the movies in which the absolute difference(using abs() function) between the `IMDb_rating` and `Metacritic` columns is less than 0.5. Refer to this link to know how abs() funtion works - https://www.geeksforgeeks.org/abs-in-python/ .
#     - Sort these values in a descending order of `Avg_rating` and retain only the movies with a rating equal to or greater than `8` and store these movies in a new dataframe `UniversalAcclaim`.
#     

# In[45]:


# Change the scale of MetaCritic
movies['MetaCritic']=movies['MetaCritic']/10
movies['MetaCritic']


# In[50]:


movies['IMDb_rating']


# In[56]:


# Find the average ratings
movies['Avg_rating']=movies.loc[:,['MetaCritic','IMDb_rating']].mean(axis=1)
Avg_rating


# In[57]:


movies.head()


# In[58]:


#Sort in descending order of average rating
movies.sort_values(by='Avg_rating', ascending=False, inplace=True)
movies.head()


# In[63]:


# Find the movies with metacritic-Imdb rating < 0.5 and also with an average rating of >= 8 (sorted in descending order)
UniversalAcclaim=movies[abs(movies['MetaCritic']-movies['IMDb_rating'])<0.5]
UniversalAcclaim[(abs(movies['MetaCritic']- movies['IMDb_rating']) < 0.5) & (movies['Avg_rating']>=8)].sort_index()[0:5]


# In[68]:


UniversalAcclaim.sort_values(by='Avg_rating',ascending=False,inplace=True)
UniversalAcclaim.reset_index(drop=True, inplace=True)
UniversalAcclaim[0:10]


# **`Checkpoint 2:`** Can you spot a `Star Wars` movie in your final dataset?

# - ### Subtask 2.4: Find the Most Popular Trios - I
# 
# You're a producer looking to make a blockbuster movie. There will primarily be three lead roles in your movie and you wish to cast the most popular actors for it. Now, since you don't want to take a risk, you will cast a trio which has already acted in together in a movie before. The metric that you've chosen to check the popularity is the Facebook likes of each of these actors.
# 
# The dataframe has three columns to help you out for the same, viz. `actor_1_facebook_likes`, `actor_2_facebook_likes`, and `actor_3_facebook_likes`. Your objective is to find the trios which has the most number of Facebook likes combined. That is, the sum of `actor_1_facebook_likes`, `actor_2_facebook_likes` and `actor_3_facebook_likes` should be maximum.
# Find out the top 5 popular trios, and output their names in a list.
# 

# In[75]:


# Write your code here
movies['Total_likes']=movies.loc[:,['actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes']].sum(axis=1)
movies.head()


# In[78]:


top_popular_actors=movies.sort_values(by='Total_likes',ascending=False,ignore_index=True).loc[0:4,:]
top_popular_actors


# In[72]:


top_popular_trios=movies.sort_values(by='Total_likes',ascending=False,ignore_index=True).loc[0:4,['actor_1_name',
'actor_2_name','actor_3_name']].values.tolist()
top_popular_trios


# - ### Subtask 2.5: Find the Most Popular Trios - II
# 
# In the previous subtask you found the popular trio based on the total number of facebook likes. Let's add a small condition to it and make sure that all three actors are popular. The condition is **none of the three actors' Facebook likes should be less than half of the other two**. For example, the following is a valid combo:
# - actor_1_facebook_likes: 70000
# - actor_2_facebook_likes: 40000
# - actor_3_facebook_likes: 50000
# 
# But the below one is not:
# - actor_1_facebook_likes: 70000
# - actor_2_facebook_likes: 40000
# - actor_3_facebook_likes: 30000
# 
# since in this case, `actor_3_facebook_likes` is 30000, which is less than half of `actor_1_facebook_likes`.
# 
# Having this condition ensures that you aren't getting any unpopular actor in your trio (since the total likes calculated in the previous question doesn't tell anything about the individual popularities of each actor in the trio.).
# 
# You can do a manual inspection of the top 5 popular trios you have found in the previous subtask and check how many of those trios satisfy this condition. Also, which is the most popular trio after applying the condition above? Write your answers in the markdown cell provided below.

# **Write your answers below.**
# 
# - **`No. of trios that satisfy the above condition:`** (3 Trios)
# 
# - **`Most popular trio after applying the condition:`** (['Leonardo DiCaprio','Tom Hardy','Joseph Gordon-Levitt'])

# **`Optional:`** Even though you are finding this out by a natural inspection of the dataframe, can you also achieve this through some *if-else* statements to incorporate this. You can try this out on your own time after you are done with the assignment.

# In[ ]:


# Your answer here (optional and not graded)


# - ### Subtask 2.6: Runtime Analysis
# 
# There is a column named `Runtime` in the dataframe which primarily shows the length of the movie. It might be intersting to see how this variable this distributed. Plot a `histogram` or `distplot` of seaborn to find the `Runtime` range most of the movies fall into.

# In[85]:


# Runtime histogram/density plot
plt.figure(figsize=[8,4])
d=sns.distplot(movies['Runtime'],color='blue')
d.axes.set_title("Movie Runtime Analysis",fontsize=15)
plt.show()


# **`Checkpoint 3:`** Most of the movies appear to be sharply 2 hour-long.

# - ### Subtask 2.7: R-Rated Movies
# 
# Although R rated movies are restricted movies for the under 18 age group, still there are vote counts from that age group. Among all the R rated movies that have been voted by the under-18 age group, find the top 10 movies that have the highest number of votes i.e.`CVotesU18` from the `movies` dataframe. Store these in a dataframe named `PopularR`.

# In[11]:


# Write your code here
content_r=movies[movies['content_rating']=='R']
PopularR=content_r.sort_values(by='CVotesU18',ascending=False,ignore_index=True)[0:10]
PopularR[0:10]


# **`Checkpoint 4:`** Are these kids watching `Deadpool` a lot?

#  

# ## Task 3 : Demographic analysis
# 
# If you take a look at the last columns in the dataframe, most of these are related to demographics of the voters (in the last subtask, i.e., 2.8, you made use one of these columns - CVotesU18). We also have three genre columns indicating the genres of a particular movie. We will extensively use these columns for the third and the final stage of our assignment wherein we will analyse the voters across all demographics and also see how these vary across various genres. So without further ado, let's get started with `demographic analysis`.

# -  ###  Subtask 3.1 Combine the Dataframe by Genres
# 
# There are 3 columns in the dataframe - `genre_1`, `genre_2`, and `genre_3`. As a part of this subtask, you need to aggregate a few values over these 3 columns. 
# 1. First create a new dataframe `df_by_genre` that contains `genre_1`, `genre_2`, and `genre_3` and all the columns related to **CVotes/Votes** from the `movies` data frame. There are 47 columns to be extracted in total.
# 2. Now, Add a column called `cnt` to the dataframe `df_by_genre` and initialize it to one. You will realise the use of this column by the end of this subtask.
# 3. First group the dataframe `df_by_genre` by `genre_1` and find the sum of all the numeric columns such as `cnt`, columns related to CVotes and Votes columns and store it in a dataframe `df_by_g1`.
# 4. Perform the same operation for `genre_2` and `genre_3` and store it dataframes `df_by_g2` and `df_by_g3` respectively. 
# 5. Now that you have 3 dataframes performed by grouping over `genre_1`, `genre_2`, and `genre_3` separately, it's time to combine them. For this, add the three dataframes and store it in a new dataframe `df_add`, so that the corresponding values of Votes/CVotes get added for each genre.There is a function called `add()` in pandas which lets you do this. You can refer to this link to see how this function works. https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.add.html
# 6. The column `cnt` on aggregation has basically kept the track of the number of occurences of each genre.Subset the genres that have atleast 10 movies into a new dataframe `genre_top10` based on the `cnt` column value.
# 7. Now, take the mean of all the numeric columns by dividing them with the column value `cnt` and store it back to the same dataframe. We will be using this dataframe for further analysis in this task unless it is explicitly mentioned to use the dataframe `movies`.
# 8. Since the number of votes can't be a fraction, type cast all the CVotes related columns to integers. Also, round off all the Votes related columns upto two digits after the decimal point.
# 

# In[12]:


# Create the dataframe df_by_genre
column_list=[]
for i in movies.columns:
    if i.startswith('ge')|i.startswith('CV')|i.startswith('V'):
        column_list.append(i)

df_by_genre=movies.loc[:,column_list]        
df_by_genre.head()        


# In[13]:


# Create a column cnt and initialize it to 1
df_by_genre['cnt']=1
df_by_genre.head()


# In[19]:


# Group the movies by individual genres
df_by_g1=df_by_genre.groupby('genre_1').sum()
df_by_g2=df_by_genre.groupby('genre_2').sum()
df_by_g3=df_by_genre.groupby('genre_3').sum()


# In[115]:


# Add the grouped data frames and store it in a new data frame
df_by_g4=df_by_g1.add(df_by_g2,fill_value=0)
df_add=df_by_g4.add(df_by_g3,fill_value=0)
df_add.head()


# In[116]:


# Extract genres with atleast 10 occurences
genre_top10=df_add[df_add['cnt']>=10]
genre_top10.head(10)


# In[117]:


# Take the mean for every column by dividing with cnt 
count_column=genre_top10['cnt'] 
genre_top10=genre_top10.div(genre_top10['cnt'], axis='index')
genre_top10.head()


# In[118]:


# Rounding off the columns of Votes to two decimals
genre_top10=genre_top10.apply(lambda x: round(x, 2), axis=0)
genre_top10.drop(columns='cnt',inplace=True)
genre_top10.head()


# In[119]:


# Converting CVotes to int type
col_cvotes_list=[]
for i in genre_top10.columns:
    if i.startswith('CVotes'):
        col_cvotes_list.append(i)

genre_top10[col_cvotes_list]=genre_top10[col_cvotes_list].astype('int')
genre_top10.head()


# If you take a look at the final dataframe that you have gotten, you will see that you now have the complete information about all the demographic (Votes- and CVotes-related) columns across the top 10 genres. We can use this dataset to extract exciting insights about the voters!

# -  ###  Subtask 3.2: Genre Counts!
# 
# Now let's derive some insights from this data frame. Make a bar chart plotting different genres vs cnt using seaborn.

# In[120]:


cnt=count_column.tolist()
genre_top10['cnt']=cnt


# In[128]:


# Countplot for genres
plt.figure(figsize=[10,8])
sns.barplot(x=genre_top10.index, y=genre_top10.cnt, color='brown')
plt.title('Genres with their count', fontsize=15)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()


# **`Checkpoint 5:`** Is the bar for `Drama` the tallest?

# -  ###  Subtask 3.3: Gender and Genre
# 
# If you have closely looked at the Votes- and CVotes-related columns, you might have noticed the suffixes `F` and `M` indicating Female and Male. Since we have the vote counts for both males and females, across various age groups, let's now see how the popularity of genres vary between the two genders in the dataframe. 
# 
# 1. Make the first heatmap to see how the average number of votes of males is varying across the genres. Use seaborn heatmap for this analysis. The X-axis should contain the four age-groups for males, i.e., `CVotesU18M`,`CVotes1829M`, `CVotes3044M`, and `CVotes45AM`. The Y-axis will have the genres and the annotation in the heatmap tell the average number of votes for that age-male group. 
# 
# 2. Make the second heatmap to see how the average number of votes of females is varying across the genres. Use seaborn heatmap for this analysis. The X-axis should contain the four age-groups for females, i.e., `CVotesU18F`,`CVotes1829F`, `CVotes3044F`, and `CVotes45AF`. The Y-axis will have the genres and the annotation in the heatmap tell the average number of votes for that age-female group. 
# 
# 3. Make sure that you plot these heatmaps side by side using `subplots` so that you can easily compare the two genders and derive insights.
# 
# 4. Write your any three inferences from this plot. You can make use of the previous bar plot also here for better insights.
# Refer to this link- https://seaborn.pydata.org/generated/seaborn.heatmap.html. You might have to plot something similar to the fifth chart in this page (You have to plot two such heatmaps side by side).
# 
# 5. Repeat subtasks 1 to 4, but now instead of taking the CVotes-related columns, you need to do the same process for the Votes-related columns. These heatmaps will show you how the two genders have rated movies across various genres.
# 
# You might need the below link for formatting your heatmap.
# https://stackoverflow.com/questions/56942670/matplotlib-seaborn-first-and-last-row-cut-in-half-of-heatmap-plot
# 
# -  Note : Use `genre_top10` dataframe for this subtask

# In[181]:


# 1st set of heat maps for CVotes-related columns
male_cvote_genre=genre_top10.groupby(genre_top10.index)['CVotesU18M','CVotes1829M','CVotes3044M','CVotes45AM'].mean()
female_cvote_genre=genre_top10.groupby(genre_top10.index)['CVotesU18F','CVotes1829F','CVotes3044F','CVotes45AF'].mean()

ax1.get_shared_y_axes().join(ax1,ax2)
g1=sns.heatmap(male_cvote_genre, cmap="Greens",annot=True, fmt='d')
g1.set_ylabel('Genres',fontsize=10)
g1.set_xlabel('Male age group',fontsize=10)
plt.show()

g2=sns.heatmap(female_cvote_genre, cmap="Greens",annot=True, fmt='d')
g2.set_ylabel('')
g2.set_xlabel('Female age group',fontsize=10)
plt.show()


# **`Inferences:`** A few inferences that can be seen from the heatmap above is that males have voted more than females, and Sci-Fi appears to be most popular among the 18-29 age group irrespective of their gender. What more can you infer from the two heatmaps that you have plotted? Write your three inferences/observations below:
# - Inference 1:U18M voted more than U18F
# - Inference 2:Age ranging from 18-44 have voted most irrespective of their gender
# - Inference 3:Sci-fi has a lesser count compare the other genres, but it has higest votes

# In[189]:


# 2nd set of heat maps for Votes-related columns
male_vote_genre=genre_top10.groupby(genre_top10.index)['VotesU18M','Votes1829M','Votes3044M','Votes45AM'].mean()
female_vote_genre=genre_top10.groupby(genre_top10.index)['VotesU18F','Votes1829F','Votes3044F','Votes45AF'].mean()


g1=sns.heatmap(male_vote_genre, cmap="Greens",annot=True)
g1.set_ylabel('Genres',fontsize=10)
g1.set_xlabel('Male age group',fontsize=10)
plt.show()

g2=sns.heatmap(female_vote_genre, cmap="Greens",annot=True)
g2.set_ylabel('')
g2.set_xlabel('Female age group',fontsize=10)
plt.show()


# **`Inferences:`** Sci-Fi appears to be the highest rated genre in the age group of U18 for both males and females. Also, females in this age group have rated it a bit higher than the males in the same age group. What more can you infer from the two heatmaps that you have plotted? Write your three inferences/observations below:
# - Inference 1:Animation genres has been voted steadily in Female gender but in Male as age increase                 avg. rating is decrease
# - Inference 2:In the age group 30-44, most of the avg. rating is around 7.7 to 7.8 
# - Inference 3:As age increases, the avg.rating is decreases in both M & F
# - Inference 4: U18 gives high rating to all genres compare to other age groups

# -  ###  Subtask 3.4: US vs non-US Cross Analysis
# 
# The dataset contains both the US and non-US movies. Let's analyse how both the US and the non-US voters have responded to the US and the non-US movies.
# 
# 1. Create a column `IFUS` in the dataframe `movies`. The column `IFUS` should contain the value "USA" if the `Country` of the movie is "USA". For all other countries other than the USA, `IFUS` should contain the value `non-USA`.
# 
# 
# 2. Now make a boxplot that shows how the number of votes from the US people i.e. `CVotesUS` is varying for the US and non-US movies. Make use of the column `IFUS` to make this plot. Similarly, make another subplot that shows how non US voters have voted for the US and non-US movies by plotting `CVotesnUS` for both the US and non-US movies. Write any of your two inferences/observations from these plots.
# 
# 
# 3. Again do a similar analysis but with the ratings. Make a boxplot that shows how the ratings from the US people i.e. `VotesUS` is varying for the US and non-US movies. Similarly, make another subplot that shows how `VotesnUS` is varying for the US and non-US movies. Write any of your two inferences/observations from these plots.
# 
# Note : Use `movies` dataframe for this subtask. Make use of this documention to format your boxplot - https://seaborn.pydata.org/generated/seaborn.boxplot.html

# In[192]:


# Creating IFUS column
movies['IFUS']=movies['Country'].apply(lambda x:'USA'if x=='USA' else 'non-USA')
movies.head()


# In[220]:


# Box plot - 1: CVotesUS(y) vs IFUS(x)
plt.figure(figsize=[10,10])
fig, axes=plt.subplots(nrows=1,ncols=1)
a1=sns.boxplot(x='IFUS',y='CVotesUS', data=movies, color='teal')
a1.axes.set_title('Dist.of votes from USA People', fontsize=12)
a1.set_ylabel('CVoteUS',fontsize=10)
a1.set_xlabel('IFUS',fontsize=10)
plt.show()

a2=sns.boxplot(x='IFUS',y='CVotesnUS', data=movies, color='pink')
a2.axes.set_title('Dist.of votes from non-USA People', fontsize=12)
a2.set_ylabel('CVotenUS',fontsize=10)
a2.set_xlabel('IFUS',fontsize=10)
plt.show()
plt.tight_layout()


# **`Inferences:`** Write your two inferences/observations below:
# - Inference 1: USA movies have great no.of votes from USA & non-USA people.
# - Inference 2: Both plots shows some outliers for USA movies.
# - Inference 3: There is difference between the no.of votes from USA people for USA & non-USA movies.
#                USA people voted less in no.for non-USA movies.

# In[226]:


# Box plot - 2: VotesUS(y) vs IFUS(x)
plt.figure(figsize=[10,10])
fig, axes=plt.subplots(nrows=1,ncols=1)
a1=sns.boxplot(x='IFUS',y='VotesUS', data=movies, color='teal')
a1.axes.set_title('Dist.of votes from USA People', fontsize=12)
a1.set_ylabel('VoteUS',fontsize=10)
a1.set_xlabel('IFUS',fontsize=10)
plt.show()

a2=sns.boxplot(x='IFUS',y='VotesnUS', data=movies, color='pink')
a2.axes.set_title('Dist.of votes from non-USA People', fontsize=12)
a2.set_ylabel('VotenUS',fontsize=10)
a2.set_xlabel('IFUS',fontsize=10)
plt.show()
plt.tight_layout()


# **`Inferences:`** Write your two inferences/observations below:
# - Inference 1: Median rating from USA people is higher than non-USA people
# - Inference 2: Both USA & non-USA people have rated non-USA movies less than that of USA movies.

# -  ###  Subtask 3.5:  Top 1000 Voters Vs Genres
# 
# You might have also observed the column `CVotes1000`. This column represents the top 1000 voters on IMDb and gives the count for the number of these voters who have voted for a particular movie. Let's see how these top 1000 voters have voted across the genres. 
# 
# 1. Sort the dataframe genre_top10 based on the value of `CVotes1000`in a descending order.
# 
# 2. Make a seaborn barplot for `genre` vs `CVotes1000`.
# 
# 3. Write your inferences. You can also try to relate it with the heatmaps you did in the previous subtasks.
# 
# 
# 

# In[241]:


# Sorting by CVotes1000
genre_top10_Cvotes=genre_top10.sort_values(by='CVotes1000',ascending=False)


# In[243]:


# Bar plot
plt.figure(figsize=[10,6])
sns.barplot(x=genre_top10_Cvotes.index, y=genre_top10_Cvotes.CVotes1000, color='teal')
plt.title('Top 1000 Voters Vs Genres', fontsize=15)
plt.xlabel('Movie Genre', fontsize=12)
plt.ylabel('CVotes1000', fontsize=12)
plt.show()


# **`Inferences:`** Write your inferences/observations here.
# 1) Sci-Fi is most popular amonngst top 1000 voters.
# 2) Romance genre has been voted the least from the top 1000 voters.

# **`Checkpoint 6:`** The genre `Romance` seems to be most unpopular among the top 1000 voters.

# 
# 
# 

# With the above subtask, your assignment is over. In your free time, do explore the dataset further on your own and see what kind of other insights you can get across various other columns.
