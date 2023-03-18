import requests
import json
import random
import datetime
from PIL import Image
from io import BytesIO
from datetime import date, datetime, timedelta
from random import randrange

from flask import Flask, jsonify, render_template, make_response, send_file

# Assuming NASA started taking pictures  between Jun 16, 1995 and Mar 18, 2023

def random_date():
    today = datetime.now().strftime("%Y/%m/%d")
    todaynew = datetime.strptime(today, "%Y/%m/%d")
    start = datetime.strptime("1995/06/16", "%Y/%m/%d")
    delta = todaynew - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
#    return start + timedelta(seconds=random_second)
    return (start + timedelta(seconds=random_second)).strftime("%Y-%m-%d")

#api_date = random_date()
#print(api_date)

#app = Flask(__name__)
app = Flask(
    __name__,
    template_folder="templates"
)


@app.route("/")
def home():
#    return {
#        "greeting": ["hello", "world"],
#        "date": date.today()
#    }
    return render_template(
        'index.html',
        title='Flask-Login Tutorial.',
        body="You are now logged in!"
    )


@app.route('/apod', methods=['GET'])
def myapod():
# calling API with date parameter
    api_date = random_date()
    print("api_date: ", api_date)
#    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=xxxxxxxx&date=2023-02-10')  
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=xxxxxxxx&date={api_date}")
#    json_data = json.load(r.text)
    json_data = r.json()
    image_url = json_data["hdurl"]
    explanation = json_data["explanation"]
#    response = requests.get(image_url)
#    img = Image.open(BytesIO(response.content))
#    img = Image.open(requests.get(image_url, stream=True).raw)
#    return send_file(img, mimetype='image/jpg')       
    return render_template(
        'apod.html',
        title='Flask-Login Tutorial.',
        explanation=explanation,
        image_url=image_url
    )

# return image_url

if __name__ == "__main__":
    app.run()

