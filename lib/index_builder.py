from math import log10

# TODO: multithreading

class IndexBuilder:
	def __init__(self):
		self.index = {}
		self.N = 0
	
	def add_posting(self, term, docid):
		if term not in self.index:
			self.index[term] = {
				"idf": 0,
				"df": 0,
				"postings": []
			}
		
		if docid not in self.index[term]["postings"]:
			self.index[term]["postings"].append(docid)

	def update_df_idf(self, term):
		if term in self.index:
			self.index[term]["df"] = len(self.index[term]["postings"])
			self.index[term]["idf"] = log10((self.N / self.index[term]["df"]))

	def process(self, docs):
		self.N = len(docs)
		term_docid_vector = [(token, i + 1) for i, doc in enumerate(docs) for token in doc]
		
		for term_docid in term_docid_vector:
			term, docid = term_docid
			self.add_posting(term, docid)

		for term in list(self.index.keys()):
			self.update_df_idf(term)
