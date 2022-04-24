from dotenv import load_dotenv
from os import environ
from lib.preprocessor import Preprocessor
from lib.reader import Reader
from lib.index_builder import IndexBuilder
from lib.query_processor import QueryProcessor
import pickle

if __name__ == '__main__':
	load_dotenv()

	r = Reader(collection_path=environ.get("COLLECTION_PATH"))
	stopwords = list(filter(lambda s: s != " ", r.read_file(environ.get("STOPWORDS_PATH")).splitlines()))
	p = Preprocessor(stopwords=stopwords)

	r.mkdir(environ.get("DUMPS_PATH"))

	preprocessed_docs = None

	if not r.path_exists(environ.get("PREPROCESSED_DUMP")):
		docs = r.get_documents()
		abstract = r.read_file(docs[0])

		abstracts = []
		for doc in docs:
			abstracts.append(r.read_file(doc))

		preprocessed_docs = p.preprocess_pipe(abstracts)
	
		with open(r.resolve_path(environ.get("PREPROCESSED_DUMP")), "wb") as output:
			pickle.dump(preprocessed_docs, output)
	else:
		with open(r.resolve_path(environ.get("PREPROCESSED_DUMP")), "rb") as input:
			preprocessed_docs = pickle.load(input)

	print(preprocessed_docs[180], len(preprocessed_docs[180]))

	index = None
	if not r.path_exists(environ.get("INDEX_DUMP")):
		i = IndexBuilder()
		i.process(preprocessed_docs)

		index = i.index

		with open(r.resolve_path(environ.get("INDEX_DUMP")), "wb") as output:
				pickle.dump(i.index, output)
		
	else:
		with open(r.resolve_path(environ.get("INDEX_DUMP")), "rb") as input:
				index = pickle.load(input)

	print(index["bootstrap"])
	q = QueryProcessor(preprocessor=p, index=index)
	print(q.process("diabetes and obesity"))