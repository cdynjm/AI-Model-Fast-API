import os
import shutil
import traceback

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
json_dir = os.path.join(project_root, 'json')

app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
CORS(app)


@app.route('/')
def home():
    title = "Chatbot API"
    message = "The API is running smoothly 🚀"
    return render_template("home.html", title=title, message=message)