from datetime import date
from datetime import datetime
import re

import numpy as np  
import pandas as pd 
from PIL import Image
import plotly.express as px  
import plotly.graph_objects as go
import streamlit as st  
import time

from plotly.subplots import make_subplots

# Read CSV file into pandas and extract timestamp data
dfSentiment = ### YOUR LINE OF CODE HERE
dfSentiment['timestamp'] = [datetime.strptime(dt, '%Y-%m-%d') for dt in dfSentiment['timestamp'].tolist()]

# Multi-select columns to build chart
col_list = ### YOUR LINE OF CODE HERE #### Extract columns into a list

r_sentiment = re.compile(".*sentiment")
sentiment_cols = ### YOUR LINE OF CODE HERE

r_post = re.compile(".*post")
post_list = ### YOUR LINE OF CODE HERE

r_perc= re.compile(".*perc")
perc_list = list(filter(r_perc.match, col_list))

r_close = re.compile(".*close")
close_list = list(filter(r_close.match, col_list))

r_volume = re.compile(".*volume")
volume_list = list(filter(r_volume.match, col_list))

sentiment_cols = sentiment_cols + post_list
stocks_cols = ### YOUR LINE OF CODE HERE

# Config for page
st.set_page_config(
    page_title= ### YOUR LINE OF CODE HERE
    page_icon='✅',
    layout='wide',
)

with st.sidebar:
    # FourthBrain logo to sidebar
    fourthbrain_logo = Image.open('./images/fourthbrain_logo.png')
    st.image([fourthbrain_logo], width=300)

    # Date selection filters
    start_date_filter = st.date_input(
        ### YOUR LINE OF CODE HERE
        min(dfSentiment['timestamp']),
        min_value=min(dfSentiment['timestamp']),
        max_value=max(dfSentiment['timestamp'])
        )
        

    end_date_filter = st.date_input(
        'End Date',
        max(dfSentiment['timestamp']),
        min_value=min(dfSentiment['timestamp']),
        max_value=max(dfSentiment['timestamp'])
        )

    sentiment_select = ### YOUR LINE OF CODE HERE
    stock_select = ### YOUR LINE OF CODE HERE

# Banner with TSLA and Reddit images
tsla_logo = ### YOUR LINE OF CODE HERE
reddit_logo = Image.open('./images/reddit_logo.png')
st.image([tsla_logo, reddit_logo], width=200)

# dashboard title
### YOUR LINE OF CODE HERE

## dataframe filter
# start date
dfSentiment = dfSentiment[dfSentiment['timestamp'] >= datetime(start_date_filter.year, start_date_filter.month, start_date_filter.day)]
    
# end date
dfSentiment = ### YOUR LINE OF CODE HERE
dfSentiment = dfSentiment.reset_index(drop=True)


# creating a single-element container
placeholder = ### YOUR LINE OF CODE HERE

# near real-time / live feed simulation
for i in range(1, len(dfSentiment)-1):

    # creating KPIs
    last_close =  dfSentiment['close'][i]
    last_close_lag1 = dfSentiment['close'][i-1]
    last_sentiment = ### YOUR LINE OF CODE HERE
    last_sentiment_lag1 = ### YOUR LINE OF CODE HERE


    with placeholder.container():

        # create columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label='Sentiment Score',
            value=round(last_sentiment, 3),
            delta=round(last_sentiment_lag1, 3),
        )
        
        kpi2.metric(
            label='Last Closing Price',
            ### YOUR LINE 1 OF CODE HERE
            ### YOUR LINE 2 OF CODE HERE
        )
        

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        
        with fig_col1:
            # Add traces
            fig=make_subplots(specs=[[{"secondary_y":True}]])


            fig.add_trace(                               
                go.Scatter(                          
                x=dfSentiment['timestamp'][0:i],
                y=dfSentiment[sentiment_select][0:i],
                name=sentiment_select,
                mode='lines',                            
                hoverinfo='none',                        
                )              
            )

            if sentiment_select.startswith('perc') == True:
                ### YOUR LINE OF CODE HERE

            elif sentiment_select in sentiment_cols:
                ### YOUR LINE OF CODE HERE

            elif sentiment_select in post_list:
                yaxis_label = 'Volume'

            fig.layout.yaxis.title=yaxis_label
                                          
            if stock_select.startswith('perc') == True:
                fig.add_trace(                               
                    go.Scatter(                          
                    x=dfSentiment['timestamp'][0:i],
                    y=dfSentiment[stock_select][0:i],
                    name=stock_select,
                    mode='lines',                            
                    hoverinfo='none', 
                    yaxis='y2',                    
                    ) 
                )
                fig.layout.yaxis2.title='% Change Stock Price ($US)'
            
            elif stock_select == 'volume':
                fig.add_trace(                               
                    go.Scatter(                          
                    x=dfSentiment['timestamp'][0:i],
                    y=dfSentiment[stock_select][0:i],
                    name=stock_select,
                    mode='lines',                            
                    hoverinfo='none', 
                    yaxis='y2',                    
                    ) 
                )
                
                fig.layout.yaxis2.title="Shares Traded"


            else:
                fig.add_trace(                               
                    go.Scatter(                          
                    x=dfSentiment['timestamp'][0:i],
                    y=dfSentiment[stock_select][0:i],
                    name=stock_select,
                    mode='lines',                            
                    hoverinfo='none', 
                    yaxis='y2',                    
                    ) 
                )

                fig.layout.yaxis2.title='Stock Price ($USD)'


            fig.layout.xaxis.title='Timestamp'

            # write the figure throught streamlit
            ### YOUR LINE OF CODE HERE


        st.markdown('### Detailed Data View')
        st.dataframe(dfSentiment.iloc[:, 1:][0:i])
        time.sleep(1)
