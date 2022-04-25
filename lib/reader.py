from pathlib import Path

class Reader:
	"""
	Simple module responsible for file handling
	"""
	def __init__(self, collection_path):
		self.path = collection_path
		self.p = Path(self.path)
		pass

	def get_documents(self):
		return sorted([doc for doc in self.p.iterdir() if doc.is_file()], key=lambda i: int(i.stem))

	def read_file(self, file):
		f = Path(file)
		# TODO: check for encoding
		return f.read_text()

	def path_exists(self, path):
		p = Path(path)
		return p.exists()

	def resolve_path(self, path):
		p = Path(path)
		return p.resolve()

	# additional utility
	def mkdir(self, path):
		Path(path).mkdir(parents=True, exist_ok=True)