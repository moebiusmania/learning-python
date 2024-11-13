from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/t/<float:celsius>', methods=['GET'])
def convert_to_kelvin(celsius):
    # kelvin = celsius + 273.15
    return jsonify({
        'celsius': celsius,
        # 'kelvin': kelvin
    }), 200

@app.route('/')
def home():
    return 'Temperature API is running. Use /t/<celsius> to convert temperatures.'

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0') 