import pandas as pd
import numpy as np

# Import data, field set as Emoji 
df = pd.read_csv('Emoji_Sentiment_Data_1.csv', index_col='Emoji')
# print (df.loc['1F602'])

#################################
########## FUNCTIONS ############
#################################

# Input: emoji itself
# Output: positive/negative/neutral
def get_sentiment(emoji):
	# find max of the pos/neg/neutral percentages
	row_data = df.loc[emoji]
	percent_pos = row_data['Percent_Positive']
	percent_neutral = row_data['Percent_Neutral']
	percent_neg = row_data['Percent_Negative']
	percent_max = max(percent_pos, percent_neutral, percent_neg)

	if percent_max == percent_pos:
		return "Positive"
	elif percent_max == percent_neutral:
		return "Neutral"
	else:
		return "Negative"
	
#################################
########## TESTING ##############
#################################

# Test get_sentiment
def test_get_sentiment():
	for emoji, data in df.iterrows():
		print(emoji)
		print (get_sentiment(emoji))
	