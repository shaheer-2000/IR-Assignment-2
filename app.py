from flask import Flask, request, jsonify
from dotenv import load_dotenv
from os import environ
from index import q

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def get_docs():
	if "query" not in request.json:
		return { "error": "ERROR!" }
	return jsonify(q.process(request.json["query"], alpha=float(environ.get("THRESHOLD_VALUE"))))
	# return { "ok": "OK!" }

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
	