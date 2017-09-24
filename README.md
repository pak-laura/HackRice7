
# HackRice7
The Project that we decided to develop in this Hackathon was to predict the price of a particular stock index for the future based on the Tweets and the sentimental values that they associate with that company at that given point of time.

# Why did we decide to build this?
We developed this application because of the growing influence of algorithmic-based trading in the market and the ability of the public perception to affect the stock ticker at any given time during the day.
This is an ongoing project and would constantly require tweaking and improvement to keep up with the current standards.

# How did we make it?
We made this by using the various publicly available APIs--here's a big shoutout to all the companies that provided an opportunity for us to use their datasets or APIs to improve our project.
 Some of the important APIs and libraries used in the development of the project are:
 1. Twitter API
 2. Tweepy
 3. Numpy
 4. MatplotLib
 5. Keras
 6. Tensorflow
 
# What is the Workflow?

* The data for every company listed in NASDAQ is available in Google Finance, and we make calls to the URL mentioned in the program to obtain trading information regarding that particular company.
The URL is used to obtain the CSV file for that particular company. A CSV file would provide with all the necessary data to predict the future price such as the opening, high, closing prices. Though the CSV could provide us with more data, we choose to only use these 3 data points.
* The Company ticker name or NASDAQ listed name will allow the user to make an API call using the Twitter API to search for tweets mentioning that company. We make use of the Tweepy library of Python to take full advantage of its searching and indexing abilities. We save the tweets with those particular keywords in a CSV file along with the user who tweeted it and the timestamp.
* This Twitter CSV File is passed on to the sentiment analyzer. In this stage we leverage the NLTK library available in Python to use Natural Language Processing to classify each tweet in the file as either Positive, Negative or Neutral.
* The sentiment analysis returns a compound value for each tweet which is an equalization of the positive and negative qualities of that tweet. These values are essential to the process of Machine Learning. The sentiment analysis values are stored in another CSV file so that the model can be used towards the final training of the prediction model.
* For the purpose of Machine Learning and predicting future data, we use a regression model which would have a linear regression model and a backpropagation network, also known as a deep learning neural network. The model is trained using Keras, which we chose to run on a TensorFlow backend. We fit in the predicted data in the model curve.
We show that there is a significant relationship between the stock prices and twitter feeds based on that company. This leads us to believe that people’s perception of a company and its product could affect its stock prices and thus enable investors to make the right call.
* We built the frontend mainly to provide the user with an intuitive interface with which to allow the user to monitor their stocks and see the projected stock prices. This allows them to make informed decisions on buying and selling their shares.

# Where do we go from here?
We have also used long short-term memory (LSTM), a recurrent neural network (RNN), to build a Keras- and TensorFlow-based stock price predictor that takes data from over a 12 or so years in order to predict stock prices accurately. This would also take into consideration the variable factors present around the user and the need to evolve. 
The ability to pull new data from various sources and aggregate them all provides a robust data source and thus improves the estimation accuracy of the system. This coupled with Artificial Intelligence could provide better results and thus eliminate human error.

