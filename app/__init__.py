from flask import Flask, request
from app.wikipedia.finding_similar_documents import similar_documents, text_popularity_coefficient
from app.wikipedia.start import wiki

app = Flask(__name__, instance_relative_config=True)
config = app.config
config.from_object('config')
config.from_pyfile('config.py')
app.register_blueprint(wiki)


@app.route('/idea_popularity', methods=['POST'])
def idea_popularity_coefficient():
    text = request.form['text']
    return text_popularity_coefficient(text)


@app.route('/hello')
def hello_world():
    return 'Hello World'