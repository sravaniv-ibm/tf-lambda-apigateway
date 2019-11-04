from flask_lambda import FlaskLambda
from flask import request, json, jsonify

app = FlaskLambda(__name__)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello Lambda from simple-flask!"})


@app.route('/welcome')
def welcome():
    return jsonify({"message": "Welcome Sravani to AWS Lambda!"})


if __name__ == '__main__':
    app.run(debug=True)