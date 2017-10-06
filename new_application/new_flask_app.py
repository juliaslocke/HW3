import requests
import json
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/music')
def choose_source():
	return render_template('blank_template.html')

@app.route('/musicresults', methods= ['POST','GET'])
def find_news():
	if request.method == 'GET':
		result = request.args
		name = result.get('name')
		term = result.get('term')
		radio = result.getlist('media')
		params = {'term':term, 'media':radio, 'limit': 10, 'format':'json'}
		info = requests.get('https://itunes.apple.com/search?', params=params)
		x = json.loads(info.text)
		return render_template('results_screen.html', results=x['results'], resultcount=x['resultCount'], name=name, term=term)

