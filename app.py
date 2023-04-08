from flask import Flask, render_template, make_response
import json
from pathlib import Path


app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/api/<year>')
def api(year):
    d = json.loads(Path('d.json').read_text())

    d_filtered = [x for x in d if int(x["Year"][0:4]) >= int(year)]
    resp = make_response(d_filtered)

    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp
