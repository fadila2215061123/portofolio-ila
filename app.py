import os
from os.path import join, dirname 
from dotenv import load_dotenv 

from flask import Flask, render_template, request, jsonify 
from pymongo import MongoClient 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f'Contact from {name} ({email}): {message}') 
    return jsonify({'msg': 'Your message has been sent!'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001, debug=True)  
