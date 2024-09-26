from flask import Flask, jsonify

app = Flask(__name__)




@app.route("/ola")
def hello():
    return jsonify({"menssage": "ola"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)