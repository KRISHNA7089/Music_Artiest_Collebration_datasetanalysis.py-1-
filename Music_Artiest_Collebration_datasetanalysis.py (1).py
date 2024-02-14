#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


df=pd.read_csv('artists.csv')
df


# In[4]:


df.shape


# In[5]:


df.dtypes


# In[6]:


df['collab_songs']=df['collab_songs'].astype(float)


# In[7]:


df['collab_songs'].dtypes


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


df


# In[13]:


df.rename(columns={'type':'type of Gender'},inplace=True)


# In[14]:


df.columns


# In[15]:


df.describe()


# In[16]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# # In Data Analysis what all things we do
# 1. Missing values
# 2. Explore about the numerical variables
# 3. Explore about the categorical variable
# 4. Finding the relationship between features
# 5. Also taking various parameter fing the relationship between two or more factor 

# In[17]:


df1=pd.read_csv('collaborations.csv')
df1


# In[18]:


df1.head()


# In[19]:


df1.columns


# In[20]:


end_df = pd.merge(df,df1,on='collab_songs',how='left')#on feature say that which features are you want to combine that two table
#How feature basically specify weathers you are focuse on that<<left or right or inners>>


# In[21]:


end_df


# In[22]:


end_df.head()


# In[23]:


end_df.describe()


# In[24]:


end_df.shape


# In[25]:


end_df.isnull().sum()
# pd.isnull(end_df).sum()#it is also type of write 


# In[26]:


end_df.dropna(inplace=True)


# In[27]:


end_df.isnull().sum()


# In[28]:


end_df.info()


# In[29]:


end_df.dtypes


# In[30]:


end_df.columns


# In[31]:


end_df.country.value_counts()


# In[32]:


#find out the indexing of country name
country_name = end_df.country.value_counts().index
country_name


# In[33]:


con_val = end_df.country.value_counts().values
con_val


# In[34]:


##Pie chart-top 3 country just using zomoto
import matplotlib
matplotlib.rcParams['figure.figsize']=(10,7)
plt.pie(con_val[:5],labels=country_name[:5],autopct='%1.2f%%')
plt.show()


# # Observation
# 1 United Kingdom are those country which has singing  song are most of the people

# In[67]:


end_df[['artist','artist1', 'artist2','country','type of Gender']].describe()


# In[37]:


end_df.groupby(['country'],as_index=False)['type of Gender'].sum().sort_values(by='type of Gender',ascending=True)


# In[38]:


k = sns.countplot(x='type of Gender',data=end_df)

sns.set(rc={'figure.figsize':(16,8)})
for bars in k.containers:
    k.bar_label(bars)


# In[69]:


end_df.groupby(['type of Gender']).size().reset_index()


# In[70]:


end_df.groupby(['country']).size().reset_index()


# In[40]:


end_df.groupby(['artist','country', 'collab_songs', 'type of Gender', 'genres']).size().reset_index()


# In[41]:


#After i do in order to convert this into a dataframe
ratings=end_df.groupby(['artist','country', 'collab_songs', 'type of Gender', 'genres']).size().reset_index().rename(columns={0:'totalNumber'})


# In[42]:


ratings.head()


# In[43]:


## countplot
sns.set(rc={'figure.figsize':(19,8)})
sns.countplot(x='country',data=ratings,palette=['black','red','orange','green','green'])


# In[44]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(19,7)
sns.barplot(x="collab_songs",y="totalNumber",data=ratings)


# In[45]:


contary_ana = df.groupby(['country','collab_individuals','type of Gender']).size().reset_index().rename(columns={0:'Number'})


# In[46]:


contary_ana


# In[47]:


sns.set(rc={'figure.figsize':(16,9)})
sns.countplot(x='collab_individuals',data=contary_ana,palette=['black','red','orange','green','green'])


# # Observation
# 1. maximum 65 man united state are collab_individuals of song
# 2. maximum 60 woman united state are collab_individuals song
# 3. maximum 10 man united state are collab_individuals of song
# 4. maximum 12 woman united state are collab_individuals song

# In[74]:


sns.set(rc={'figure.figsize':(16,9)})
sns.countplot(x='collab_songs',data=ratings,palette=['black','red','orange','green','green'])


# In[49]:


#Find the maximun artist sing song on the basis of country gender 
end_df[['artist','country','type of Gender']].groupby(['artist','country','type of Gender']).size().reset_index()


# In[50]:


#we are also fing taking parameter artist, artist1,artist2 consider three parameter which country are maximum artist on the basis of type of Gender
end_df[['artist','artist1', 'artist2','country','type of Gender']].groupby(['artist','artist1', 'artist2','country','type of Gender']).size().reset_index()


# In[51]:


end_df.groupby(['artist','country','collab_songs','genres'],as_index=False)['type of Gender'].sum().sort_values(by='type of Gender',ascending=True).head(6)


# In[52]:


end_df.groupby(['artist1', 'country','genres'],as_index=False)['type of Gender'].sum().sort_values(by='type of Gender',ascending=True)


# In[53]:


end_df.groupby(['artist2', 'country','genres'],as_index=False)['type of Gender'].sum().sort_values(by='type of Gender',ascending=True)


# In[54]:


end_df.groupby(['artist','artist1', 'artist2','type of Gender'],as_index=False)['country'].sum().sort_values(by='country',ascending=True)


# In[55]:


## Create a pia chart of top 5 artist
val_1 = end_df.artist.value_counts().index
# val_1
val_2 = end_df.artist.value_counts().values
# val_2


# In[56]:


matplotlib.rcParams['figure.figsize']=(12,9)
plt.pie(val_2[:10],labels=val_1[:10],autopct="%1.2f")
plt.show()


# In[57]:


## Create a pia chart of top 5 artist
val_1 = end_df.artist1.value_counts().index
# val_1
val_2 = end_df.artist1.value_counts().values
# val_2


# In[58]:


matplotlib.rcParams['figure.figsize']=(12,9)
plt.pie(val_2[:10],labels=val_1[:10],autopct="%1.2f")
plt.show()


# In[59]:


## Create a pia chart of top 5 artist
val_1 = end_df.artist2.value_counts().index
# val_1
val_2 = end_df.artist2.value_counts().values
# val_2


# In[60]:


matplotlib.rcParams['figure.figsize']=(12,9)
plt.pie(val_2[:10],labels=val_1[:10],autopct="%1.2f")
plt.show()


# In[ ]:





# In[61]:


val_s = end_df.genres.value_counts().index
# val_s
val_v = end_df.genres.value_counts().values
# val_v


# In[62]:


matplotlib.rcParams['figure.figsize']=(21,17)
plt.pie(val_v[:10],labels=val_s[:10],autopct="%1.2f")
plt.show()


# In[63]:


#we are also fing which country artiest are collab_individuals
end_df.groupby(['collab_individuals'],as_index=False)['country'].sum().sort_values(by='country',ascending=True)


# In[64]:


#we are also fing which country artiest are collab_individuals
end_df.groupby(['collab_songs'],as_index=False)['country'].sum().sort_values(by='country',ascending=True)


# In[76]:


sns.set(rc={'figure.figsize':(16,9)})
sns.countplot(x='type of Gender',data=ratings,palette=['black','red','orange','green','green'])


# In[65]:


end_df.groupby(['type of Gender'],as_index=False)['country'].sum().sort_values(by='country',ascending=True)


# In[ ]:





# In[ ]:





# In[ ]:




