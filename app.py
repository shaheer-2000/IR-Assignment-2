from flask import Flask, request, jsonify
from dotenv import load_dotenv
from os import environ
from index import init

load_dotenv()
app = Flask(__name__)

if __name__ == '__main__':
	q = init()

	@app.route("/", methods=["GET", "POST"])
	def get_docs():
		if "query" not in request.json:
			return { "error": "ERROR!" }
		return jsonify(q.process(request.json["query"], alpha=float(environ.get("THRESHOLD_VALUE"))))
		# return { "ok": "OK!" }


	app.run(port=5000)
	