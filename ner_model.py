from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

def extract_items(sentence):

	# sentence = "Book a train from Delhi to 26/11/2018 Indore via Banglore."
	ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
	iob_tagged = tree2conlltags(ne_tree)
	# ne_tree = conlltags2tree(iob_tagged)

	extracted = {}
	extracted['Locations'] = []
	extracted['Dates'] = []
	extracted['Travel_type'] = []

	for i in iob_tagged:
		if 'GPE' in i[2]:
			extracted['Locations'].append(i[0])

		if i[1] == 'NN':
			extracted['Travel_type'].append(i[0])

		if i[1] == 'CD':
			extracted['Dates'].append(i[0])

	# for key, value in extracted.items():
	# 	print(key + " : " + str(value) + '\n')
	return extracted