from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fetch_gross_profit', methods=['GET'])
def fetch_gross_profit():
    ticker = request.args.get('ticker')
    # Replace this with your actual logic to fetch gross profit
    gross_profit = get_gross_profit(ticker)
    return jsonify({'gross_profit': gross_profit})

def get_gross_profit(ticker):
    # Your logic to fetch gross profit for the given ticker
    # For example, you might fetch data from an API or database
    return "123456"  # Replace this with actual fetched value

if __name__ == '__main__':
    app.run(debug=True)
