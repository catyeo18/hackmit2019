import pandas as pd
import numpy as np
from itertools import islice

# Import data, field set as Emoji 
df = pd.read_csv('Emoji_Sentiment_Data_1.csv', index_col='Emoji')
# print (df.loc['1F602'])

#################################
########## FUNCTIONS ############
#################################

# Input: emoji 
# Output: positive/negative/neutral sentiment
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

# Input: emoji
# Output: full name
def get_emoji_name(emoji):
	row_data = df.loc[emoji]
	return row_data['Emoji_Name']

# More advanced than get_sentiment
# by differentiating emoticons (faces) from other emoji icons
HAPPY = ('HAPPY', 'JOY', 'CHEER', 'SMILE', 'SMILING', 'GRIN', 'GRINNING', 'WINKING', 'SMIRKING')
SAD = ('SAD', 'TIRED', 'WEARY', 'CRY', 'CRYING', 'PERSEVERING')
ANGRY = ('ANGRY', 'MAD', 'UPSET', 'UNAMUSED')

def get_emotion(emoji):
	row_data = df.loc[emoji]

	# if it is an emoticon, further analysis
	if row_data['Emoji_Type'] == 'Emoticons':
		name = get_emoji_name(emoji).split()
		for word in name:
			if word in HAPPY:
				return "Happy"
			if word in SAD:
				return "Sad"
			if word in ANGRY:
				return "Angry"

	return get_sentiment(emoji)
	
#################################
########## TESTING ##############
#################################

# Test get_sentiment
def test_get_sentiment():
	for emoji, data in df.iterrows():
		print(emoji)
		print (get_sentiment(emoji))

# Test get_sentiment
def test_get_emoji_name():
	for emoji, data in df.iterrows():
		print(emoji)
		print (get_emoji_name(emoji))
	
def test_get_emotion():
	for emoji, data in islice(df.iterrows(), 25):
		print(emoji)
		print (get_emotion(emoji))
		print()

test_get_emotion()