from app import app
import datetime
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

@app.route('/random')
def randomDate():
   year = random.choice(range(2000, 2025))
   month = random.choice(range(1,13))
   day = random.choice(range(1,31))
   testdate = datetime.datetime(year,month,day).strftime('%s')
   return str(testdate)
