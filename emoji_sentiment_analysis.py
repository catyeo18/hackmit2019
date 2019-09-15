import pandas as pd
import numpy as np
from itertools import islice

# Import data, field set as Emoji 
df = pd.read_csv('Emoji_Sentiment_Data_1.csv', index_col='Unicode')
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
		return "POSITIVE"
	elif percent_max == percent_neutral:
		return "NEUTRAL"
	else:
		return "NEGATIVE"

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
				return "HAPPY"
			if word in SAD:
				return "SAD"
			if word in ANGRY:
				return "ANGRY"

	return get_sentiment(emoji)

# Output: keywords (exclude filler words like 'face', 'of', 'and') + sentiment
def get_keywords(emoji):
	row_data = df.loc[emoji]
	name = get_emoji_name(emoji).split()
	keywords = set()
	keywords.add(get_emotion(emoji))
	fillers = ['AND', 'BUT', 'FACE', 'OF', 'WITH', 'SYMBOL', 'HEAVY', 'A', 'IN']
	for word in name:
		if word not in fillers:
			keywords.add(word)

	return keywords

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

def test_get_keywords():
	for emoji, data in islice(df.iterrows(), 125):
		print(emoji)
		print (get_keywords(emoji))
		print()

# test_get_keywords()