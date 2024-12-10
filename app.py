from flask import Flask, request, jsonify
from utils import add, subtract

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Arithmetic API!"})

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    try:
        result = add(data["a"], data["b"])
        return jsonify({"operation": "addition", "result": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400

@app.route("/subtract", methods=["POST"])
def subtract_numbers():
    data = request.get_json()
    try:
        result = subtract(data["a"], data["b"])
        return jsonify({"operation": "subtraction", "result": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400

if __name__ == "__main__":
    app.run(debug=True)