class QueryProcessor:
	def __init__(self, preprocessor, index):
		self.preprocessor = preprocessor
		self.index = index

	def process(self, query, alpha=0.04):
		tokens = self.preprocessor.preprocess(query)
		print(tokens)
		query_vector = {}
		for t in tokens:
			query_vector[t] = tokens.count(t) 

			# ( / self.index[t]["idf"])

		s = 0
		for t in query_vector:
			s += query_vector[t]

		for t in tokens:
			query_vector[t] /= s

		tokens = sorted(list(set(tokens)))
		doc_vectors = {}

		for t in tokens:
			for p in self.index[t]["postings"]:
				if p not in doc_vectors:
					doc_vectors[p] = 0
				
				# print((t, p))
				doc_vectors[p] += round(self.index[t]["postings"][p]["tfidf"] * query_vector[t], 3)

		return list(filter(lambda x: x[1] >= alpha, sorted(doc_vectors.items(), key=lambda p: p[0])))