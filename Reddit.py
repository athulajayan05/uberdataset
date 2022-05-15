from warnings import filters
import praw
from datetime import datetime, timezone
import pandas as pd
import time
import tzlocal
from tzlocal import get_localzone
import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 


reddit = praw.Reddit(client_id='4cwdjOEFDdEHPtyZY9h59Q', client_secret='ZWxQWVPeFl-wpRuhkpylb7dAq3KgAQ', user_agent='final project')

st.set_page_config(
    page_title = 'Data visualization-620 Dashboard',
    layout = 'wide'
)

st.title("Covid-19 Home Testing Kits Reviews on reddit application")



import pytz
data = {"Title": [], "Post_Text" : [],"ID" : [], "Score" :[], "Total_Comments": [], "Post_URL" : [],"Post_Created" :[]}

for submission in reddit.subreddit("all").search("COVID-19 home test kits"):
    data["Title"].append(submission.title)
    data["Post_Text"].append(submission.selftext)
    data["ID"].append(submission.id)
    data["Score"].append(submission.score)
    data["Total_Comments"].append(submission.num_comments)
    data["Post_URL"].append(submission.url)
    unix_time = submission.created_utc
    data["Post_Created"].append(datetime.fromtimestamp(unix_time,pytz.timezone('US/Eastern')))
st.dataframe(data)




# Date_filter = st.selectbox("Select the date", reddit.subreddit("all").search("COVID-19 home test kits", time_filter = "day" ))



st.title("Comments for each post")

comments_data = {"post_comments" : [], "ID" : [], "Score" :[], "Comment_Created" : []}
for id in data["ID"]:
    submission = reddit.submission(id=id)
    #print(submission1)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments_data["post_comments"].append(comment.body)
        comments_data["ID"].append(comment.id)
        comments_data["Score"].append(comment.score)
        unix_time = comment.created_utc
        comments_data["Comment_Created"].append(str(datetime.fromtimestamp(unix_time)))
st.dataframe(comments_data)


