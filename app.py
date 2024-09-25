from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({"message": "API Flask Using Docker"})

