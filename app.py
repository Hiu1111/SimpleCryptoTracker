from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/') #Sets the homepage 
def home():
    return "Welcome to the Cryptocurrency Portfolio Tracker!"

@app.route('/crypto-prices', methods=['GET']) #second page which brings you to the list of cryptoprices 
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price' #fetches the data using coingecko api 
    params = {'ids': 'bitcoin,ethereum', 'vs_currencies': 'usd'} #shows which coins are being fetched 
    response = requests.get(url, params=params).json() #makes a get request to get the data 
    return render_template('index.html', prices=response) #passes the data over to html to display the data passed to it

if __name__ == '__main__':
    app.run(debug=True)


    

