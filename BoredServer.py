import json
from IAmBored import give_suggestion 


from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_suggestion(): 
	[line, sub] = give_suggestion()
	return json.dumps({'line' : line, 'subtitle' : sub})

