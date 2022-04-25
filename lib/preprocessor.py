import spacy

class Preprocessor:
	"""
	Simple preprocessing pipeline making use spacy's robust
	pipelining and tokenization API

	Simple removes punctuation, stopwords, and tokenizes with lemma
	"""
	def __init__(self, stopwords):
		self.stopwords = stopwords
		self.punctuations = "!@#$%^&*()_+-=,./<>?;':\"[]{}\|`~`"
		self.nlp = spacy.load("en_core_web_sm")

	def tokenize(self, text):
		doc = self.nlp(text)
		return [token.lemma_.lower() for token in doc if token.text.isalpha() and token.lemma_ is not None]
	
	def is_stopword(self, token):
		return token in self.stopwords
	
	def is_punctuation(self, token):
		return token in self.punctuations

	def preprocess(self, text):
		tokens = self.tokenize(text)
		return list(filter(lambda t: not self.is_stopword(t) and not self.is_punctuation(t), tokens))

	def reducer_pipe(self, doc):
		return [token.lemma_.lower() for token in doc if token.is_alpha and token.text.lower() not in self.stopwords]

	def preprocess_pipe(self, texts):
		preproc_pip = []
		for doc in self.nlp.pipe(texts, n_process=2, batch_size=100):
			preproc_pip.append(self.reducer_pipe(doc))
		
		return preproc_pip
