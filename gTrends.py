'''must pip install pytrends'''

#example in github, testing
from pytrends.request import TrendReq

#log in to Google
pytrend= TrendReq()

#create payload, capture API tokens? only for time, region, related queries
pytrend.build_payload(kw_list=['iPhone', 'iPad','Apple','iOS'],timeframe ='now 1-d')

interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())
