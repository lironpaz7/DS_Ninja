from flask import Flask, request
from model import predict

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome'


@app.route('/predict')
def run_prediction():
    title = request.args.get('title', default='')
    pred = predict(title)
    return f'Seniority prediction for {title}: {pred}'


if __name__ == '__main__':
    app.run()
