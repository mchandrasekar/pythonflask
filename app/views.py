from app import app
from datetime import date
import random
import time
import json

@app.route('/')
@app.route('/index')
def index():
    currentTime = int(time.time())
    jsonObj = {}
    jsonObj['Time'] = currentTime
    #return json.dumps(jsonObj)
    return str(currentTime)
