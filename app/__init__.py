import os
import shutil
import traceback
import json
import random
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from app.train import train_model
from fuzzywuzzy import fuzz
import re

app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
CORS(app)

@app.route('/')
def home():
    title = "Chatbot API"
    message = "The API is running smoothly 🚀"
    return render_template("home.html", title=title, message=message)

