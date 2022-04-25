from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ

# The main entry point for the VSM
from index import q

app = Flask(__name__)
CORS(app)

# API handler - simple
@app.route("/", methods=["GET", "POST"])
def get_docs():
	if "query" not in request.json or q is None:
		return { "error": "ERROR!" }

	alpha = environ.get("THRESHOLD_VALUE")
	if "alpha" in request.json and request.json["alpha"] is not None:
		alpha = request.json["alpha"]

	return jsonify(q.process(request.json["query"], alpha=float(alpha)))

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
	