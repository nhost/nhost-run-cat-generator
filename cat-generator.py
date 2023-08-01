from flask import Flask, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/cat')
def generate_cat_picture():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    image_url = response.json()[0]['url']

    # Get the image content
    image_content = requests.get(image_url).content

    # Send the image file
    return send_file(BytesIO(image_content), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
