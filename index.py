from flask import Flask, render_template, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URI = os.getenv('DATABASE_URI')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)