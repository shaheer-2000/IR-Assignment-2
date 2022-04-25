from os import environ
from lib.preprocessor import Preprocessor
from lib.reader import Reader
from lib.index_builder import IndexBuilder
from lib.query_processor import QueryProcessor
import pickle

# Initialize the reader module
r = Reader(collection_path=environ.get("COLLECTION_PATH"))
# Read & Parse stopwords list
stopwords = list(filter(lambda s: s != " ", r.read_file(environ.get("STOPWORDS_PATH")).splitlines()))
# Initialize the preprocessing pipeline
p = Preprocessor(stopwords=stopwords)

# Create the dumps direcctory if it doesnt exist
r.mkdir(environ.get("DUMPS_PATH"))

preprocessed_docs = None

# Check to see if dump exists, if not create dump for preprocessed docs
if not r.path_exists(environ.get("PREPROCESSED_DUMP")):
	docs = r.get_documents()
	preprocessed_docs = []
	for doc in docs:
		d = r.read_file(doc)
		preprocessed_docs.append(p.preprocess(d))

	# Commented to disable batch processing
	# preprocessed_docs = preprocess_pipe(abstracts)

	with open(r.resolve_path(environ.get("PREPROCESSED_DUMP")), "wb") as output:
		pickle.dump(preprocessed_docs, output)
else:
	with open(r.resolve_path(environ.get("PREPROCESSED_DUMP")), "rb") as input:
		preprocessed_docs = pickle.load(input)

index = None

# Check to see if index exists, if not create and dump
if not r.path_exists(environ.get("INDEX_DUMP")):
	i = IndexBuilder()
	i.process(preprocessed_docs)

	index = i.index

	with open(r.resolve_path(environ.get("INDEX_DUMP")), "wb") as output:
			pickle.dump(i.index, output)
	
else:
	with open(r.resolve_path(environ.get("INDEX_DUMP")), "rb") as input:
			index = pickle.load(input)

# Initialize the query processor and make it available
q = QueryProcessor(preprocessor=p, index=index)