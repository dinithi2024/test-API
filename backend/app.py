from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests, so React can connect to this backend

# Sample destinations data
destinations = [
    {"id": 1, "name": "Paris", "country": "France"},
    {"id": 2, "name": "Tokyo", "country": "Japan"},
    {"id": 3, "name": "New York", "country": "USA"}
]

# GET route to retrieve destinations
@app.route('/api/destinations', methods=['GET'])
def get_destinations():
    return jsonify(destinations)

# POST route to add new destination
@app.route('/api/destinations', methods=['POST'])
def add_destination():
    new_destination = request.json
    destinations.append(new_destination)
    return jsonify({"message": "Destination added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
