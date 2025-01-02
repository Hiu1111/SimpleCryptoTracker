from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Cryptocurrency Portfolio Tracker!"

@app.route('/crypto-prices', methods=['GET'])
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin,ethereum', 'vs_currencies': 'usd'}
    response = requests.get(url, params=params).json()
    return render_template('index.html', prices=response)

if __name__ == '__main__':
    app.run(debug=True)

    

