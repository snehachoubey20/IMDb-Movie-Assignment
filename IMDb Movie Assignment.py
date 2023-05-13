#!/usr/bin/env python
# coding: utf-8

# In[ ]:


IMDb Movie Assignment


# In[ ]:


##Reading the data


# In[7]:


import warnings

warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


movies = pd.read_csv(r'C:\Users\sneha\Downloads\Movie+Assignment+Data (1).csv')


# In[9]:


movies.head()


# In[ ]:


##Identifying the data types and null values


# In[11]:


movies.shape


# In[12]:


movies.info()


# In[13]:


movies.describe()


# In[ ]:


##Data Analysis

##These numbers in the budget and gross are too big, compromising its readability. 
##Let's convert the unit of the budget and gross columns from $ to million $ first.


# In[14]:


movies["budget"] = movies["budget"] / 1000000
movies["Gross"] = movies["Gross"] / 1000000
movies.head()


# In[ ]:


##Create a new column called profit which contains the difference of the two columns: gross and budget.
##Sort the dataframe using the profit column as reference.
##Extract the top ten profiting movies in descending order and store them in a new dataframe - top10.
##Plot a scatter or a joint plot between the columns budget and profit and write a few words on what you observed.
##Extract the movies with a negative profit and store them in a new dataframe - neg_profit


# In[15]:


# Create the new column named 'profit' by subtracting the 'budget' column from the 'gross' column

movies["profit"] = movies["Gross"] - movies["budget"]

# Sort the dataframe with the 'profit' column as reference using the 'sort_values' function. Make sure to set the argument
#'ascending' to 'False'

movies.sort_values(by="profit",ascending=False)


# In[16]:


# Get the top 10 profitable movies by using position based indexing. Specify the rows till 10 (0-9)

movies.sort_values(by="profit",ascending=False).iloc[0:10]


# In[17]:


#Plot profit vs budget

sns.scatterplot(data=movies,x="profit",y="budget")
plt.show()


# In[ ]:


##The dataset contains the 100 best performing movies from the year 2010 to 2016. 
##However scatter plot tells a different story. 
##You can notice that there are some movies with negative profit. 
##Although good movies do incur losses, but there appear to be quite a few movie with losses.
##What can be the reason behind this? 
##Lets have a closer look at this by finding the movies with negative profit.


# In[18]:


#Find the movies with negative profit

movies[movies["profit"] < 0]


# In[ ]:


##Checkpoint 1: Can you spot the movie Tangled in the dataset? 
##You may be aware of the movie 'Tangled'. 
##Although its one of the highest grossing movies of all time, it has negative profit as per this result. 
##If you cross check the gross values of this movie (link: https://www.imdb.com/title/tt0398286/), you can see that the gross in the dataset accounts only for the domestic gross and not the worldwide gross.
##This is true for may other movies also in the list.    


# In[19]:


## The general audience and critics
##As a part of this subtask, 
##you are required to find out the highest rated movies which have been liked by critics and audiences alike.


# In[ ]:


##Firstly you will notice that the MetaCritic score is on a scale of 100 whereas the IMDb_rating is on a scale of 10. First convert the MetaCritic column to a scale of 10.
##Now, to find out the movies which have been liked by both critics and audiences alike and also have a high rating overall, you need to -
##Create a new column Avg_rating which will have the average of the MetaCritic and Rating columns
##Retain only the movies in which the absolute difference(using abs() function) between the IMDb_rating and Metacritic columns is less than 0.5. Refer to this link to know how abs() funtion works - https://www.geeksforgeeks.org/abs-in-python/ .
##Sort these values in a descending order of Avg_rating and retain only the movies with a rating equal to higher than 8 and store these movies in a new dataframe UniversalAcclaim.


# In[20]:


# Change the scale of MetaCritic
movies["MetaCritic"] = movies["MetaCritic"] / 10


# In[21]:


# Find the average ratings
movies["Avg_rating"] = (movies["MetaCritic"] + movies["IMDb_rating"]) / 2
movies.head()


# In[22]:


#Sort in descending order of average rating

movies.sort_values(by="Avg_rating",ascending=False)


# In[23]:


# Find the movies with metacritic-rating < 0.5 and also with the average rating of >8

movies[(movies["MetaCritic"] < 0.5) & (movies["Avg_rating"] > 8)]


# In[ ]:


##Find the Most Popular Trios - I
##You're a producer looking to make a blockbuster movie. 
##There will primarily be three lead roles in your movie and you wish to cast the most popular actors for it. 
##Now, since you don't want to take a risk, you will cast a trio which has already acted in together in a movie before. 
##The metric that you've chosen to check the popularity is the Facebook likes of each of these actors.

##The dataframe has three columns to help you out for the same, viz. actor_1_facebook_likes, actor_2_facebook_likes, and actor_3_facebook_likes. 
##Your objective is to find the trios which has the most number of Facebook likes combined. 
##That is, the sum of actor_1_facebook_likes, actor_2_facebook_likes and actor_3_facebook_likes should be maximum. 
##Find out the top 5 popular trios, and output their names in a list.


# In[24]:


#checking head to see if any actor_x_facebook_likes rows have NaN values

movies.head()


# In[26]:


# Write your code here
#cleaning actor_x_facebook_likes rows coz they have NaN values
movies ["actor_1_facebook_likes"] = movies["actor_1_facebook_likes"].replace(np.NaN,0)
movies ["actor_2_facebook_likes"] = movies["actor_2_facebook_likes"].replace(np.NaN,0)
movies ["actor_3_facebook_likes"] = movies["actor_3_facebook_likes"].replace(np.NaN,0)

movies.head()


# In[27]:


#adding a new row here to sum all the facebook likes of the trio of every movie
movies["facebook_likes_combined"] = movies["actor_1_facebook_likes"] + movies["actor_2_facebook_likes"] + movies["actor_3_facebook_likes"]


# In[28]:


#sorting by facebook_likes_combined and getting top 5 trio
movies.sort_values(by="facebook_likes_combined",ascending=False).iloc[0:5]


# In[ ]:


##Find the Most Popular Trios - II
##In the previous subtask you found the popular trio based on the total number of facebook likes. 
##Let's add a small condition to it and make sure that all three actors are popular. 
##The condition is none of the three actors' Facebook likes should be less than half of the other two.


# In[ ]:


#3No. of trios that satisfy the above condition: 2

##Most popular trio after applying the condition: Leonardo DiCaprio Tom Hardy Joseph Gordon-Levitt


# In[ ]:


## Runtime Analysis
##There is a column named Runtime in the dataframe which primarily shows the length of the movie. 
##It might be intersting to see how this variable this distributed. 
##Plot a histogram or distplot of seaborn to find the Runtime range most of the movies fall into.


# In[29]:


# Runtime histogram/density plot
sns.distplot(movies["Runtime"])
plt.show()


# In[ ]:


##most of the popular movies are around 2 hours long. 


# In[ ]:


## R-Rated Movies

##Although R rated movies are restricted movies for the under 18 age group, still there are vote counts from that age group. 
#3Among all the R rated movies that have been voted by the under-18 age group, find the top 10 movies that have the highest number of votes i.e.CVotesU18 from the movies dataframe. 
##Store these in a dataframe named PopularR.


# In[30]:


# Write your code here

PopularR = movies[(movies["content_rating"] == "R") & (movies["CVotesU18"] > 0)].sort_values(by="CVotesU18",ascending=False).iloc


# In[31]:


##Demographic analysis

# Create the dataframe df_by_genre
df_by_genre = movies.iloc[0:,11:14].join(movies.iloc[0:,16:60])


# In[32]:


# Create a column cnt and initialize it to 1
df_by_genre["cnt"] = 1


# In[33]:


# Group the movies by individual genres
df_by_g1 = df_by_genre.groupby("genre_1").sum()
df_by_g2 = df_by_genre.groupby("genre_2").sum()
df_by_g3 = df_by_genre.groupby("genre_3").sum()


# In[34]:


# Add the grouped data frames and store it in a new data frame
df_add = df_by_g1.add(df_by_g2,fill_value=0).add(df_by_g3,fill_value=0)


# In[35]:


# Extract genres with atleast 10 occurences
genre_top10 = df_add[df_add["cnt"] > 10].sort_values(by="cnt",ascending=False)
genre_top10


# In[36]:


# Take the mean for every column by dividing with cnt 
for i in range(0,44):
    genre_top10.iloc[:,i] = genre_top10.iloc[:,i] / genre_top10.iloc[:,-1]
genre_top10


# In[37]:


# Rounding off the columns of Votes to two decimals
genre_top10.iloc[:,27:44] = round(genre_top10.iloc[:,27:44],2)

# Converting CVotes to int type
genre_top10.iloc[:,0:27] = genre_top10.iloc[:,0:27].astype(int)


# In[38]:


## Genre Counts!
##Now let's derive some insights from this data frame. 
##Make a bar chart plotting different genres vs cnt using seaborn.


# Countplot for genres
genre_top10.cnt.plot.bar()


# In[39]:


##If you have closely looked at the Votes- and CVotes-related columns, you might have noticed the suffixes F and M indicating Female and Male. 
##Since we have the vote counts for both males and females, across various age groups.
##Let's now see how the popularity of genres vary between the two genders in the dataframe.

# 1st set of heat maps for CVotes-related columns
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
heatmap_m = sns.heatmap(genre_top10.iloc[:,13:23:3],annot=True,cmap="Spectral_r")
bottom, top = heatmap_m.get_ylim()
heatmap_m.set_ylim(bottom + 0.5, top - 0.5)
plt.subplot(1,2,2)
heatmap_f = sns.heatmap(genre_top10.iloc[:,14:24:3],annot=True,cmap="Spectral_r")
bottom, top = heatmap_f.get_ylim()
heatmap_f.set_ylim(bottom + 0.5, top - 0.5)
plt.show()




# In[ ]:


##Inferences: A few inferences that can be seen from the heatmap above is that males have voted more than females, and Sci-Fi appears to be most popular among the 18-29 age group irrespective of their gender. What more can you infer from the two heatmaps that you have plotted? Write your three inferences/observations below:

##Inference 1: Sci-Fi also appears to be the most popular category among males and females of age 30-44 and above 45 as well (also applies for males and females of age under 18)

##Inference 2: Thriller and action seem to the second and adventure seems to be the third favourtie category among males of age 18-29 (animation seems to be the least favourite) whereas adventure seems to be the second and animation seems to be the thrid favourite category among females of age 18-29 (crime seems to be the least favourite). This implies that males of age 18-29 would rather watch any other genre of movie than animation whereas the females of age 18-29 would rather watch any other genre of movie than crime

##Inference 3: Males of age under 18 like romantic movies the least whereas thats not the case with females under 18, who like crime movies the least.

##Inference 4: Crime movies are generally the least favourite among females of all ages except when they turn above 45. They somehow like crime movies more than animated movies which used to be their favourite in their younger days.


# In[40]:


# 2nd set of heat maps for Votes-related columns
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
heatmap_m = sns.heatmap(genre_top10.iloc[:,30:40:3],annot=True,cmap="Spectral_r")
bottom, top = heatmap_m.get_ylim()
heatmap_m.set_ylim(bottom + 0.5, top - 0.5)
plt.subplot(1,2,2)
heatmap_f = sns.heatmap(genre_top10.iloc[:,31:41:3],annot=True,cmap="Spectral_r")
bottom, top = heatmap_f.get_ylim()
heatmap_f.set_ylim(bottom + 0.5, top - 0.5)
plt.show()


# In[ ]:


##Inferences: Sci-Fi appears to be the highest rated genre in the age group of U18 for both males and females. Also, females in this age group have rated it a bit higher than the males in the same age group. What more can you infer from the two heatmaps that you have plotted? Write your three inferences/observations below:

##Inference 1:Sci-Fi appears to be the highest rated genre in males of all age groups whereas for females, after being 18+, the highest rated genre becomes animation for all other age groups.

##Inference 2: For males, animated movies are the least rated for age group under 18 whereas romantic movies become the least rated for all other age groups. For females, crime movies remain the least rated for all age groups except 45+ where that place is shockingly taken by romantic movies

##Inference 3:In general, people, irrespective of age and gender like movies more when they are younger and that liking and the tendency to give higher rating decreases over time, thereby decreasing the average rating of age groups if we go from under 18 to 45+


# In[41]:


## US vs non-US Cross Analysis

# Creating IFUS column
#initializing all columns with USA
movies["IFUS"] = "USA" 

#changing all values where country != USA
movies.loc[movies["Country"] != "USA","IFUS"] = "non-USA" 
movies


# In[42]:


# Box plot - 1: CVotesUS(y) vs IFUS(x)
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
sns.boxplot(x=movies["IFUS"],y=movies["CVotesUS"])
plt.subplot(1,2,2)
sns.boxplot(x=movies["IFUS"],y=movies["CVotesnUS"])
plt.show()


# In[ ]:


##Inference 1: From both plots, we can see that non-USA plot's IQR is slightly larger thant USA people plot
##Inference 2: From both plots, there seem to be some outliers in USA plot, suggesting that some USA movies got exceptionally high votes from USA and non-USA people


# In[43]:


# Box plot - 2: VotesUS(y) vs IFUS(x)
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
sns.boxplot(x=movies["IFUS"],y=movies["VotesUS"])
plt.subplot(1,2,2)
sns.boxplot(x=movies["IFUS"],y=movies["VotesnUS"])
plt.show()


# In[ ]:


##Inference 1: From both plots, we can see that there are some USA movies that have got exceptionally high rating from USA and non-USA people (outliers in USA plot)
##Inference 2: From both plots, USA people have roughly given ratings to non-USA movies in range (7.8-8) and USA movies in range (7.8-8.1) whereas non-USA people have roughly given ratings to non-USA movies in range(7.6-8) and USA movies in range(7.6-7.9). There seems to be trend here that states that USA people will rate USA movies higher and non-USA people will rate non-USA movies higher


# In[ ]:


## Top 1000 Voters Vs Genres
##You might have also observed the column CVotes1000. 
##This column represents the top 1000 voters on IMDb and gives the count for the number of these voters who have voted for a particular movie. Let's see how these top 1000 voters have voted across the genres.


# In[44]:


genre_top10


# In[45]:


# Sorting by CVotes1000

genre_top10.sort_values(by='CVotes1000',ascending=False)


# In[46]:


# Bar plot

plt.figure(figsize=(10,5))
sns.barplot(x=genre_top10.index,y=genre_top10["CVotes1000"])


# In[ ]:


##Inferences:-

## Sci-Fi still seems to be the highest voted category here as well, as was the case in case of heatmaps
## Same trends seen in the heatmaps are seen here with regards to adventure, action and thriller as them being the next voted genres

