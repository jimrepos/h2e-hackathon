import re
class Preprocess():
	# Strip special characters, punctuation and return content lowercase
	def reformat_submission(self, content):
		clean_content = re.sub('[^A-Za-z0-9 ]+', '', content).lower()
		return clean_content