from math import log10, sqrt

# TODO: multithreading
# length normalize tf values for documents -> tf / magnitude(doc)
# 

class IndexBuilder:
	def __init__(self):
		self.index = {}
		self.tf_doc_matrix = {}
		self.doc_norm = {}
		self.N = 0
	
	def add_posting(self, term, docid):
		if term not in self.index:
			self.index[term] = {
				"idf": 0,
				"df": 0,
				"postings": {}
			}
		
		if docid not in self.index[term]["postings"]:
			# assigning term-freq in document
			self.index[term]["postings"][docid] = {
				"tf": 1,
				"tfidf": 0
			}
		else:
			self.index[term]["postings"][docid]["tf"] += 1

	def update_df_idf(self, term):
		if term in self.index:
			self.index[term]["df"] = len(self.index[term]["postings"])
			self.index[term]["idf"] = log10((self.N / self.index[term]["df"]))

	def update_tfidf(self, term):
		if term in self.index:
			for docid in self.index[term]["postings"]:
				self.index[term]["postings"][docid]["tfidf"] = (self.index[term]["postings"][docid]["tf"] / self.doc_norm[docid]) * self.index[term]["idf"]

	def process(self, docs):
		self.N = len(docs)
		term_docid_vector = [(token, i + 1) for i, doc in enumerate(docs) for token in doc]
		
		for term_docid in term_docid_vector:
			term, docid = term_docid

			if docid not in self.tf_doc_matrix:
				self.tf_doc_matrix[docid] = {}
			if term not in self.tf_doc_matrix[docid]:
				self.tf_doc_matrix[docid][term] = 0

			self.tf_doc_matrix[docid][term] += 1

			self.add_posting(term, docid)

		for docid in self.tf_doc_matrix:
			s = 0
			for v in self.tf_doc_matrix[docid].values():
				s += v ** 2

			self.doc_norm[docid] = sqrt(s)

		for term in list(self.index.keys()):
			self.update_df_idf(term)
			self.update_tfidf(term)
