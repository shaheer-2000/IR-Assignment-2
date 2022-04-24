# IR Assignment 2
## Vector Space Model
Implemented a Vector-Space Model with tf-idf as the primary weighting scheme and Euclidean normalization for tf-values.

The [main](https://github.com/shaheer-2000/IR-Assignment-2) branch has a CLI-based input mechanism, whereas the [heroku-deployment](https://github.com/shaheer-2000/IR-Assignment-2/tree/heroku-deployment) branch has the Flask-based backend API to be deploying to heroku.

## Installation & Startup
- ``pip install -r requirements.txt``
- Create a ``.env`` file in the ``root` directory
- Set-up environment variables
- Run ``python app.py``

## Environment Variables
- ``COLLECTION_PATH`` - relative path to abstracts
- ``STOPWORDS_PATH`` - relative path to stopwords file
- ``PREPROCESSED_DUMP`` - relative path to store preprocessed object
- ``INDEX_DUMP`` - relative path to store the index object
- ``DUMPS_PATH`` - relative path to the dumps folder for the object storage
- ``THRESHOLD_VALUE`` - threshold / alpha-value for filtering
- ``FLASK_APP`` - flask app

## Libraries
- ``spacy`` - used for robut tokenization, paired with multiprocess-batch-processing, to speed up the preprocessing stage
- ``flask`` - to deploy the simple API for querying the model

## Technologies
- ``heroku`` - for hosting the backend
- ``vercel`` - for deploying the frontend
- ``materializecss`` - for a quick and simple stylized HTML mockup

## TODO / Known Issues
- ``spacy``'s lemmatization led to a few _comparatively irregular_ lemmas that lead to an increased amount of results, with the resulting similarity values varying from the Gold-Query-Set by a small amount.

## Heroku API
The [heroku API](https://vsm-ir.herokuapp.com/) is available at the provided URL and accepts ``POST`` requests at ``/`` with the body 
```json
{
	"query": <query text>,
	"alpha": <floating-point value>
}
```

## Frontend/GUI
The [GUI](https://ir-a2-frontend.vercel.app/) is available at the provided URL and was intentionally kept simple, even though there were plans of including _Summary Snippets_, but where left-out due to not being stated in the provided documentation.

## Author(s)
| <img src="https://avatars.githubusercontent.com/u/20398468?v=4" width="100" height="100" /> |
  :---: 
| [shaheer-2000 (19K-0233)](https://github.com/shaheer-2000) | 
