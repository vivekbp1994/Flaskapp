# [START gae_python37_app]
from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! This is my first google app!!'


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())


@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Imports the Google Cloud client library 
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities) 


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
