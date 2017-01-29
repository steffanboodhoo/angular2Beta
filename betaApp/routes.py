from betaApp import app
from flask import request

@app.route('/', methods=['GET'])
def handleInit():
	return 'hello'