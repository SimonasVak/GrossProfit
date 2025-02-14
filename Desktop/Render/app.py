from flask import Flask, jsonify, request
from fetch_data import fetch_all_data
import os

app = Flask(__name__)

@app.route('/api/fetch-data', methods=['POST'])
def fetch_data():
    try:
        data = request.get_json()
        ticker = data.get('ticker')
        stock_exchange = data.get('stockExchange')
        
        if not ticker or not stock_exchange:
            return jsonify({'error': 'Ticker and stock exchange are required'}), 400
            
        financial_data = fetch_all_data(ticker, stock_exchange)
        return jsonify(financial_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
