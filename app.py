from flask import Flask, request, jsonify
from urllib import response
import json
import os, sys
from flask_cors import CORS
from jinja2.utils import markupsafe

## Importing project modules
newdir = os.path.abspath(os.path.join(os.path.dirname("__file__"), './src'))
sys.path.append(newdir)
import src

markupsafe.Markup()

app = Flask(__name__)
CORS(app)

wat = src.WAT()

@app.route('/', methods=["GET"])
def hello_world():
    return "Hey! This is the WAT API"

@app.route('/paraphrase', methods=["POST"])
def paraphrase():
    data = json.loads(request.data)
    text = data['text']
    paraphrase = wat.paraphrase_text(text)
    response = {'data' :{'paraphrased': paraphrase}}
    return jsonify(response)

@app.route('/analytics', methods=['POST'])
def generateParaphrase():
    data = json.loads(request.data)
    text = data['text']
    result, top_four_words = wat.analyse(text)
    response = {'data': {'processed_text': result, 'frequent_words': top_four_words}}
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)