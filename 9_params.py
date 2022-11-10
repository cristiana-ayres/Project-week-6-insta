import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import seaborn as sns
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import math

# importing followers data base
data = pd.read_csv("followers_top_final.csv")


# creating sum of likes
sum_of_likes = []

for number in average_likes_per_post["sum_like"]:
    sum_of_likes.append(number)

# creating sum of comments
sum_of_comments = []

for number in average_comments_per_post["sum_comment"]:
    sum_of_comments.append(number)

likes_and_comments = [like + comment for like, comment in zip(sum_of_likes, sum_of_comments)]

total_followers = data.pivot_table(index=["ranking","username"], values=["followers"], aggfunc= {"followers" : ["mean"]})
total_followers.columns = total_followers.columns.droplevel()


# total_followers.columns = ["total_followers"]

# followers_multiplied = []

# for number in total_followers["total_followers"]:
#     followers_multiplied.append(number * 1000000)


# engagement = [(likes_comments * 100) / followers for likes_comments, followers in zip(likes_and_comments, followers_multiplied)]



# creating the logistic regression model
X = data[['engagement_activity','followers', 'following', 'total_posts', 'likes_per_post', 'comments_per_post']]
y = data['channel_associated_on_bio']

    # type of engagement will be generated by 2 bins based on : 
    # from 0 to 5 : low engagement = 0 
    # from 5 to 10 or higher : high engagement = 1 
    # we will have to generate this new column 

#  create the model 
logistic = linear_model.LogisticRegression()

# train the model 
logistic.fit(X,y)

# evaluate the model 
logistic.score(X,y)

# create the scaler 
scaler = StandardScaler()

# fit our data to the standard scaler 
scaler.fit(X)

# transform the data
scaler.transform(X)

scaled_X = pd.DataFrame(scaler.transform(X), columns=X.columns)



# inserting new values / instagram accounts
# predict using the logistic 1 which was trained in data that was not standardized 
logistic.predict(new_influencers)

