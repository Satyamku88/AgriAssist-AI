from flask import Flask, jsonify
import random

app = Flask(__name__)

# Mock Soil Data API
@app.route('/api/soil-data')
def soil_data():
    return jsonify({
        'moisture': random.randint(0, 100),
        'nitrogen': random.randint(0, 50),
        'temperature': random.randint(20, 40)
    })

# Mock Crop Recommendation API
@app.route('/api/recommend-crop')
def recommend_crop():
    crops = ['Wheat', 'Rice', 'Corn', 'Soybean']
    return jsonify({'crop': random.choice(crops)})

if __name__ == '__main__':
    app.run(debug=True)