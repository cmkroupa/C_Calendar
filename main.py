#main file that will conduct a sentiment_analysis using sentiment_analysis.py's functions
"""

Cameron Kroupa,
251342448,
ckroupa,
10/31/2023,
this file calls the functions in the sentiment_analysis in the proper order to conduct a sentiment analysis on the users desired files
"""

# Import the sentiment_analysis module
from sentiment_analysis import *


def main():
	#main function that will order the function calls to conduct the analysis
	keywordFilename = input("Enter Keyword Filename: ")#user desired keyword file
	
	if (keywordFilename[-4:] != ".tsv"): #error in file name
		raise Exception("Must have tsv file extension!")
	keywords = read_keywords(keywordFilename) #read in keywords dictionary with scores
	
	tweetsFilename = input("Enter Tweets Filename: ") #user desired file containing tweets
	
	if (tweetsFilename[-4:] != ".csv"): #error in file name
		raise Exception("Must have csv file extension!")
	tweets = read_tweets(tweetsFilename) #list of dictionary for each tweet

	if len(keywords) == 0 or len(tweets) == 0: #error in keyword or tweet file size (contains nothing)
		raise Exception("Tweet list or keyword dictionary is empty")
	
	tweetReportValues = make_report(tweets, keywords) #creates values to report upon

	reportFileName = input("Enter Report Filename: ") #user report file name
	
	if (reportFileName[-4:] != ".txt"): #file name error
		raise Exception("Must have txt file extension!")
	write_report(tweetReportValues, reportFileName)


main() #calls main function which will conduct all the analysis using functions in sentiment_analysis