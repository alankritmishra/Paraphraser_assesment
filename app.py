from flask import Flask, request, jsonify
from urllib import response
import json
import os, sys
from flask_cors import CORS
from jinja2.utils import markupsafe
import random
import nltk

## Importing project modules
newdir = os.path.abspath(os.path.join(os.path.dirname("__file__"), './src'))
sys.path.append(newdir)
import src

markupsafe.Markup()

app = Flask(__name__)
CORS(app)

nltk.download('stopwords')
wat = src.WAT()

f = open('db.json')
data = json.load(f)

@app.route('/', methods=["GET"])
def hello_world():
    return "Hey! This is the WAT API"

@app.route('/paraphrase', methods=["POST"])
def paraphrase():
    try:
        req = json.loads(request.data)
        uid = req['uid']
        print(uid)
        paragraphs = data[uid]
        print(paragraphs)
        result = {
            "data" :{
                "paraphrased" : paragraphs["paraphrased_paragraph"]
            }
        }
        return result
    except:
        return {"error" : "Invalid uid"}

@app.route('/analytics', methods=['POST'])
def generateParaphrase():
    data = json.loads(request.data)
    text = data['text']
    result, top_four_words = wat.analyse(text)
    response = {'data': {'processed_text': result, 'frequent_words': top_four_words, "direct_phrase": [], "similarity_index":0.3 }}
    return jsonify(response)

@app.route('/paragraph', methods=['GET'])
def generateParagraph():
    keys = data.keys()
    index = random.choice(list(keys))
    paragraph = data[index]
    result = {
        "uid": index,
        "paragraph": paragraph['paragraph']
    }
    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))