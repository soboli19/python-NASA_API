import requests
import json
from PIL import Image
from io import BytesIO
from datetime import date

from flask import Flask, jsonify, render_template, make_response, send_file

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
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=xxxxxxxx&date=2023-02-10')  
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

