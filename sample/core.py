''' This is the main module (core) '''
import helpers
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/')
@app.route('/api/<username>')

def my_microservice(username='World!'):
    return jsonify({'Hello': username})

print(str(helpers.message()))
