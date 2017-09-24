# HackRice7
The Project that we decided to develop in this Hackathon was to predict the price of a particular stock index for the future based on the Tweets and the sentimental values that they associate with that company at that given point of time.

# Why did we decide to build this?
The reason behind developiing such an application is because of the growing influence of Algorithmic based trading in the market and the ability of the public perception to affect the stock ticker at any given time during the day.
This is an ongoing project and would constantlyrequire tweaking and improvement to keep up with the current standards.

# How did we make it?
We made this by using the various APIs publicly available and a big shoutout to all the companies that provided an opportunity to use their datasets or APIs to improve our project.
 Some of the important APIs and libraries used in the development of the project are:
 1. Twitter API
 2. Tweepy
 3. Numpy
 4. MatplotLib
 5. Keras
 6. Tensorflow
 
# What is the Workflow?

* The Data for each and ever company listed in Nasdaq was available in the Google finances section and we make calls to the URL mentioned in the program to obtain trading info regarding that particular company.
The url is used to obtain the CSV Files for that particular company. This CSV file would provide with all the necessary data to predict the future price such as the opening, High, Closing price. Though the CSV would provide us with more data, we choose to only use these 3 data points.
* The Company ticker name or Nasdaq listed name will allow the user to make an API Call using the twitter API to search for tweets with those particular tweets. We make use of the Tweepy library of Python to take full advantage of the searching and indexing abilities availible in it. We save the twitter feed with those particular keywords in a csv file followed by the user who tweeted it and the timestamp.
* This twitter CSV File is passed onto the next stage which happens to be the sentiment analyzer. In this stage we leverage the NLTK library available in python to tag a tweet using Natural Language processing to classify the said tweets as either Positive, negative or Neutral.
* The sentimental analysis reveals a compound value which is an equalization of the positive and negative qualities of the tweet. This would serve as a key towards ensuring that the process of Machine learning. Sentiment Analysis value is appended to the CSV File so that the model can be used towards the final training of the prediction model.
* For the purpose of Machine learning and predicting future data, we use a regression model which would have a Back propagation network and a Linear regression model. The model is trained using Keras which serves on top of a Tensorflow Backend. We fit in the predicted data in the model curve.
We show that there is a significant relationship between the stock prices and twitter feeds based on that Company. This leads us to believe that the people perception of a company and its product could afect the prices and thus enable investors to make the right call.
* Building the Frontend is mainly used to provide the user with an intuitive interface which would allow the user to monitor his stocks see the estimated stock prices and the need to buy or sell shares

# Where do we go from here?
We have also used LSTM and RNN to build a keras and Tensorflow based Stock price predictor which takes data worth over a couple of years(12 years or so) in order to try and predict stock prices accurately. This would also take into consideration the variable factors present aorund the user and the need to evolve. 
The ability to pull new data from various sources and aggregate them all to provide a robust data source and thus improve the estimation level of the system. This coupled with Artificial Intelligenece could provide better results and thus eliminate the need or presence of human error.



