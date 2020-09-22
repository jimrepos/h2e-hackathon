import logging
import json

class Vocabulary():
	lexicon = {}

	def load_vocabulary(self):
		with open('vocabulary.json') as json_file:
			self.lexicon = json.load(json_file)

	def get_vocabulary(self):
		self.load_vocabulary()

		# order lexicon by word count in a flattened structure (as a single list)
		flat_lexicon = {**self.lexicon['positive'], **self.lexicon['negative']}

		ordered_lexicon = sorted(flat_lexicon.items(), key=lambda x: (len(x[0].split(' ')), len(x[0])), reverse=True)

		return ordered_lexicon