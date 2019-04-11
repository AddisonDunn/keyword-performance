# Addison Dunn, University of Virginia

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from collections import Counter

###### ------------------ DATA EXTRACTION --------------------- #######
# (from json; .txt file)

tweets_data_path = 'twitterdata.txt'


def extract():
	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	workset= []

	#------- COMPLICATED JSON AND LANGUAGE EXTRACTION ------#

	# for line in tweets_file:
	#     try:
	#         tweet = json.loads(line)
	#         tweets_data.append(tweet)
	#     except:
	#         continue

	# #----------------------------------------------------------------------

	

	# # print('----------------LANGUAGES-----------------')

	# # tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)

	# # tweets_by_lang = tweets['lang'].value_counts()

	# # print("LANGUAGES:")
	# # print(tweets_by_lang[0:5])
	# print('--------------------------------------------------------------')

	# tweets['workset'] = map(lambda tweet: tweet['text'], tweets_data)
	# workset = filter(None, tweets['workset'].values.tolist())
	# print('WORKSET:  ' + str(workset))

	###### -------------------- EASY READING -------------------- ########

	for line in tweets_file:
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue

	tweets = pd.DataFrame()
	tweets['workset'] = map(lambda tweet: tweet['text'], tweets_data)
	workset = filter(None, tweets['workset'].values.tolist())
	# print('WORKSET:  ' + str(workset))

	print("NUMBER OF TWEETS: " + str(len(workset)))


	###### ------------------- KEYWORD EXTRACTION --------------- #########

	phrases = []

	grammar = ('''
    NP: {<JJ>+<NN>}
    ''')
	chunkParser = nltk.RegexpParser(grammar)

	for text in workset:
		# tokens.append(nltk.pos_tag(nltk.word_tokenize(text)))
		tagged_sentence = nltk.pos_tag(nltk.word_tokenize(text))
		parse_tree = chunkParser.parse(tagged_sentence)

		for minitree in parse_tree:
			if type(minitree) == nltk.tree.Tree:
				phrases.append(" ".join([token for token, pos in minitree.leaves()]))


	# print(phrases)
	print("COUNTER: " + str(Counter(phrases)))

		#Defined grammar using regular expressions


#############################################################
if __name__ == '__main__':
    extract()

def test():
	return "test worked"