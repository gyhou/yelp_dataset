import json
import pickle
import sklearn
import numpy as np
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def address():
    '''Takes json dictionaries and return prediction values'''

    # receive input
    inputs = request.get_json(force=True)

    # get data from json
    category = inputs['category']
    review = inputs['review']
    # validate input
    assert isinstance(category, str)
    assert isinstance(review, str)

    # unpickle
    category = category.replace(" ", "_")
    filename = category+"_yelp_review_predict_star.pkl"
    infile = open(filename, "rb")
    model = pickle.load(infile)
    infile.close()

    # predict
    review_rating = model.predict([review])

    # use a dictionary to format output for json
    out = {'Category': category,
           'Review': review,
           'Predict rating': int(review_rating[0])}

    # give output to sender
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(port=9000, debug=True)
