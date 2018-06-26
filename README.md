# Twitter-Analysis
1.	First obtain authorization codes from Twitter and fill up the fields in the python code. 

2.	Run the python file changing the keywords to retrieve tweets mentioning  blockchain, bitcoin and ethereum. Make sure the output files names are changed in the script to avoid overwriting. Then merge all data in a single CSV file.  

3.	Make sure that the actual tweet is in the third column. Merge the tweets column and the location column, using excel (Location based analysis done for USA vs Rest of the world. Hence all cities in USA is transformed to USA and then concatenated with the tweets column. Similarly All the cities of other countries are changed to Rest of the world and the concatenated with the tweets)
	
5.	Do a word frequency analysis with wordfrequency.py. This will give you an initial idea of the important “issues” – some issues may have to be merged as well. E.g., references to “fraud” and “cheat” are talking about the same thing. Hence use the find_and_replace.py file where appropriate to replace similar meaning words in the tweet. Run wordfrequency.py again.  Make your final selection of issues based on highest frequencies. 

6.	 Run a lift analysis of (Bitcoin,Ethereum,issue 1,issue2,issue 3,issue 4,issue 5,issue 6) and find top three issues for each currency. Note that an issue can be associated strongly with both currencies. 

7.	Once you have identified the issues, now you have to use parserforsentiment.py to extract mentions of a currency and an issue. E.g., Bitcoin and fraud. The script asks you for (i) brand (bitcoin in this case), (ii) attribute (fraud in this case) and the number of words to retain on the right and left hand sides of the issue (the assumption being that people express their emotions within a close proximity of the attribute). Note that both inputs (brand and attribute) must be typed in lowercase. The output file should be labeled carefully, e.g., bitcoin_fraud.csv. 

8.	Now bitcoin_fraud.csv can be used with sentiment.py (on Canvas) for sentiment analysis. 

9. Now similarly for location based analysis run the parserforsentiment.py file but now brand=bitcoin (or ethereum), attribute=USA001 (or rest_of_the_world) and # words = 20 (so that the whole tweet is included). The output of this script should be a file which has tweets on bitcoin from the US. Now use sentiment analysis on this file.   
