from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')


# Bangalore
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Ahmedabad
@app.route('/get_location_names1', methods=['GET'])
def get_location_names1():
    response = jsonify({
        'locations': util.get_location_names1()

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Bangalore
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Ahmedabad
@app.route('/predict_home_price1', methods=['GET', 'POST'])
def predict_home_price1():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    size = int(request.form['size'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price1(location, total_sqft, size, bath)

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    util.load_saved_artifacts1()
    app.debug = True
    app.run()
