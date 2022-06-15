import sys
import traceback

from flask import Flask, jsonify, request
import pandas as pd
import pickle


app = Flask(__name__)

@app.route('/predict', methods=['POST']) # Create http://host:port/predict POST endpoint
def predict():

    try:
        json = request.get_json()

        vectorizer = pickle.load(open('vectorizer.pk', 'rb'))  # load CountVectorizer for preprocessing text
        model = pickle.load(open('model.pkl', 'rb'))           # load model for prediction

        # json example: [{"tweet":"Neka peva ova kuca"}, {"tweet":"Sta ce mi zivot"}, ...]
        text = pd.DataFrame(json)
        text = vectorizer.transform(text['tweet'])

        prediction = list(model.predict(text))

        return jsonify({'prediction': [int(x) for x in prediction]})

    except Exception as e:

        return jsonify({'error': str(e), 'trace': traceback.format_exc()})

if __name__ == '__main__':

    try:
        port = int(sys.argv[1])
        print(port)
    except Exception as e:
        port = 80

    app.run(host='0.0.0.0', port=port, debug=False)

