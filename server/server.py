# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import util
#
#
# app = Flask(__name__)
# CORS(app)
#
# @app.route('/classify_image', methods=['GET', 'POST'])
# def classify_image():
#     image_data = request.form['image_data']
#
#     response = jsonify(util.classify_image(image_data))
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response
#
# if __name__ == "__main__":
#     print("Starting Python Flask Server For Sports Celebrity Image Classification")
#     util.load_saved_artifacts()
#     app.run(host='192.168.63.97', port=5000)
#
#

from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)
