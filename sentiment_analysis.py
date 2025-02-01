#sentiment_analysis file that contains all the functions to conduct a sentiment analysis

"""
Cameron Kroupa,
251342448,
ckroupa,
10/31/2023,
this file is all the functions that are necessary for a sentiment analysis to be done. By creating and cleaning tweets, to analyzing, 
to reporting on the tweets, this file contains functions to complete these tasks. Its the job of another file to call the functions
in this file in a proper manner to conduct the full analysis. 
This file contains functions that:
read_keywords: read in keywords from a file and organize them with their sentiment score
clean_tweet_text: this cleans tweets by making sure all characters are in english alphabet and lowercase
calc_sentiment: calculates the sentiment for each tweet
classify: classifies a tweet as positive, negative, neutral based on sentiment value
read_tweets: reads in tweets and cleans them using the clean function
make_report: calculates values to make a report on the tweets
write_report: writes a report utilizing values created in make_report
"""


def read_keywords(keyword_file_name): 
     #read in keywords from a file and organize them with their sentiment score
     # Add your code here
	# Should return a dict of keywords.
     try:
          keywords = {}
          file = open(keyword_file_name, "r")
          while (documentLine := file.readline().strip()) != "":
               splitLine = documentLine.split("\t")
               keywords[splitLine[0]] = int(splitLine[1])
          file.close()
          return keywords
     except IOError:
          print(f"Could not open file {keyword_file_name}!")
          return {}

def clean_tweet_text(tweet_text): 
     #this cleans tweets by making sure all characters are in english alphabet and lowercase
    # Add your code here
	# Should return a string with the clean tweet text.
     tweet_text = tweet_text.lower()
     newText = ""
     for letter in tweet_text:
          if letter.isalpha() or letter == " ":
               newText += letter
     return newText

def calc_sentiment(tweet_text, keyword_dict):
    # calculates the sentiment for each tweet
    # return an integer value for the sentiment based on the keywords, and the words in the tweet
     sentimentScore = 0 
     wordsInTweet = tweet_text.split()
     for word in wordsInTweet:
          if word in keyword_dict:
               sentimentScore += keyword_dict[word]

     return sentimentScore

def classify(score):
    # classifies a tweet as positive, negative, neutral based on sentiment value
    # return a string classification for the tweet based on sentiment value
     if score > 0:
          return "positive"
     elif score < 0:
          return "negative"
     return "neutral"

def read_tweets(tweet_file_name): 
     #reads in tweets into a dictionary containg all the tweets info and cleans the tweet text using the clean function
     try:
          tweets = []
          file = open(tweet_file_name, "r")
          while (documentLine := file.readline().strip()) != "":
               splitLine = documentLine.split(",")
               tweets.append({"date" : splitLine[0],
                                "text" : splitLine[1],
                                "user" : splitLine[2],
                                "retweet" : int(splitLine[3]),
                                "favorite" : int(splitLine[4]),
                                "lang" : splitLine[5],
                                "country" : splitLine[6],
                                "state" : splitLine[7],
                                "city" : splitLine[8],
                                "lat" : splitLine[9],
                                "lon" : splitLine[10]})
               if tweets[-1]["lat"] != "NULL":
                    tweets[-1]["lat"] = float(tweets[-1]["lat"])
               if tweets[-1]["lon"] != "NULL":
                    tweets[-1]["lon"] = float(tweets[-1]["lon"])
          file.close()

          for tweet in tweets: #cleans each tweets text
               tweet["text"] = clean_tweet_text(tweet["text"]) 

          return tweets
     except IOError:
          print(f"Could not open file {tweet_file_name}!")
          return []
     
def make_report(tweet_dict, keyword_dict):
     #creates all the values to be sent to the write function to be reported in the report file

     for tweet in tweet_dict: #calculates sentiment score for each tweet
          tweet["sentiment"] = calc_sentiment(tweet["text"],keyword_dict) #add sentiment to the tweets dictionary
	
    
    # Add your code here
	# Should return a dictionary containing the report values.
     reportValues = {}
     #1) Num Tweets
     reportValues["num_tweets"] = len(tweet_dict)
     #2) Avg Sentiment Score of all Tweets
     totalSentimentScore = 0
     #3) total positive, negative, and neutral tweets based on sentiment
     numTweetsPositive = 0
     numTweetsNegative = 0
     numTweetsNeutral = 0
     #4) num tweets with atleast one fav/like
     numTweetFavd = 0
     #5) Avg sentiment score of only tweets with 1 fav/like
     sentimentSumOfFavd = 0
     #6) Num Tweets with atleast 1 retweer
     numTweetRetweeted = 0
     #7) avg sentiment of retweeted
     sentimentScoreOfRetweeted = 0
     #8) Avg Sentiment Score of Each country
     country_dict = {} #dictionary of all countries, keeps track of total tweets, and total sentiment value
          

     for tweet in tweet_dict:
          totalSentimentScore += tweet["sentiment"]

          classification = classify(tweet["sentiment"]) #adds to the classification total for positive/negative/neutral tweets
          if classification == "negative":
               numTweetsNegative += 1
          elif classification == "positive":
               numTweetsPositive += 1
          else:
               numTweetsNeutral += 1

          if tweet["favorite"] >= 1: #if tweet has been favorited then +1 to totalTweetsFavorited and add the sentimentValue to a tracker 
               numTweetFavd += 1
               sentimentSumOfFavd += tweet["sentiment"]

          if tweet["retweet"] >= 1: #same thing as favorited but with retweeted
               numTweetRetweeted += 1
               sentimentScoreOfRetweeted += tweet["sentiment"]

          if tweet["country"] in country_dict: #if the country is alreayd in country_dict add the sentiment value and +1 numTweets
               country_dict[tweet["country"]]["NumTweets"] += 1
               country_dict[tweet["country"]]["TotalSentiment"] += tweet["sentiment"]
               country_dict[tweet["country"]]["AvgSentiment"] = country_dict[tweet["country"]]["TotalSentiment"] / country_dict[tweet["country"]]["NumTweets"]
          else: #if its not in country_dict then add if its not NULL
               if tweet["country"] != "NULL":
                    country_dict[tweet["country"]] = {"AvgSentiment": tweet["sentiment"], "NumTweets" : 1.0, "TotalSentiment" : tweet["sentiment"]}



     reportValues["num_negative"] = numTweetsNegative
     reportValues["num_neutral"] = numTweetsNeutral
     reportValues["num_positive"] = numTweetsPositive
     reportValues["num_favorite"] = numTweetFavd
     reportValues["num_retweet"] = numTweetRetweeted
     if numTweetFavd != 0: #calc avg_favorite
          reportValues["avg_favorite"] = round(sentimentSumOfFavd / float(numTweetFavd), 2)
     else:
          reportValues["avg_favorite"] = "NAN"

     if reportValues["num_tweets"] != 0: #calc avg_sentiment
          reportValues["avg_sentiment"] = round(totalSentimentScore / float(reportValues["num_tweets"]), 2)
     else:
          reportValues["avg_sentiment"] = "NAN"

     if numTweetRetweeted != 0: #calc avg_retweet
          reportValues["avg_retweet"] = round(sentimentScoreOfRetweeted / float(numTweetRetweeted), 2)
     else:
          reportValues["avg_retweet"] = "NAN"  
          
     sortedCountries = sorted(country_dict.items(), key=lambda item: item[1]["AvgSentiment"], reverse=True) #sorts dictionary in order of avg sentiment
     print(sortedCountries)
     top5Countries = ""
     for i in range(0, 5): #creates the string for reportValues[top_five]
          if len(sortedCountries) - i <= 0:
               break
          top5Countries += "%s, " % (sortedCountries[i][0])
          
     
     reportValues["top_five"] = top5Countries[0:-2]

     return reportValues
       #list of countries will compare the list to dictionary countryDict to find max then will pop listOfCountries into list MaxCountries
     
def write_report(report, output_file):
    #takes in dictionary of values to be written into the report file
    #writes a report utilizing values created in make_report
     try:
          document = open(output_file, "w")
          document.write("Average sentiment of all tweets: %s\n" % (str(report["avg_sentiment"])))
          document.write("Total number of tweets: %d\n" % (report["num_tweets"]))
          document.write("Number of positive tweets: %d\n" % (report["num_positive"]))
          document.write("Number of negative tweets: %d\n" % (report["num_negative"]))
          document.write("Number of neutral tweets: %d\n" % (report["num_neutral"]))
          document.write("Number of favorited tweets: %d\n" % (report["num_favorite"]))
          document.write("Average sentiment of favorited tweets: %s\n" % (str(report["avg_favorite"])))
          document.write("Number of retweeted tweets: %d\n" % (report["num_retweet"]))
          document.write("Average sentiment of retweeted tweets: %s\n" % (str(report["avg_retweet"])))
          document.write("Top five countries by average sentiment:%s" % (report["top_five"]))
          document.close()

          print("Wrote report to %s" % (output_file))
     except IOError:
          print("Could not open file %s" % (output_file))

